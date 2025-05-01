import numpy as np
import os
import warnings

from synthesis.rqa_detector import RQA_Detector

import itertools
from collections import defaultdict

import synthesis.sonic_pi_dsl as dsl
from synthesis.rosette_integrator import iterative_synth
from synthesis.rosette_translator import translate_rosette

"""
takes collection of user extracted and built in Sonic Pi samples and emits 
a complete Sonic Pi samples and emits a complete Sonic Pi .rb program
"""

class ProgramGenerator:
    """
    Builds a Sonic Pi program from two sets of samples

    Attributes:
        samples :   Sample_File instances extracted from original track
        sonic_sample :  Sonic_Sample_File instances
        samples_folder : absolute path to where samples are on disk
        contents : accumulates generated Ruby code
    """
    def __init__(self, samples, sonic_samples, samples_folder=None):
        """
        Initialise with two sample sets and optional base folder
        """
        self.contents = ""
        self.samples = samples
        self.sonic_samples = sonic_samples
        if samples_folder != None:
            self.samples_folder = os.path.abspath(samples_folder)
        else:
            self.samples_folder = None
    
    def calc_env_duration(self, val1, val2):
        """
        Compute an ADSR stage duration, rounded to three decimals

        Args:   
            start_time : float, time of previous envelope point
            end_time   : float, time of current envelope event
        
        Returns:
            float: duration (end_time - syaty_time)
        """
        return np.round(val2-val1, 3)

    def calc_env_level(self, val1, val2, max_val):
        """
        Compute normalised level change for ADSR, rounded to 3dp
        Args:   
            start_time : float, previous envelope level
            end_level  : float, current envelope level
            max_val    : float, maximum possible level for normalisation
        
        Returns:
            float: (end_level - start_level) / max_level
        """
        print(max_val)
        return np.round((val2-val1)/max_val,3)

    def get_env(self, s):
        """
        Extract ADSR parameters from a Sample_file

        Returns:
            tuple of 8 floats:
            (start_dur, attack_dur, decay_dur, sustain_dur, release_dur, 
            attack_level, ecay_level, sustain_level
        """
        env = s.env
        start = self.calc_env_duration(0,env.start.time)
        attack = self.calc_env_duration(env.start.time, env.attack.time)
        decay = self.calc_env_duration(env.attack.time, env.decay.time)
        sustain = self.calc_env_duration(env.decay.time, env.sustain.time)
        release = self.calc_env_duration(env.sustain.time, env.release.time)
        attack_level = self.calc_env_level(env.start.level, env.attack.level, s.max_vol)
        decay_level = self.calc_env_level(env.start.level, env.decay.level, s.max_vol)
        sustain_level = self.calc_env_level(env.start.level, env.sustain.level, s.max_vol)
        return start, attack, decay, sustain, release, attack_level, decay_level, sustain_level

class LoopProgramGenerator(ProgramGenerator):
    """
    generator that writes explicit live_loops and rings in raw Ruby text
    """
    def filter_offsets(self, offsets, sample_len):
        """
        Remove any offsets that would overlap a previously scheduled play of the sample
        This Sonic Pi from getting overwhelmed by short processing times between sample plays
        Args:
            offsets : sorted list of trigger times (seconds)
            sample_len : duration of the sample (seconds)
        Returns:
            included : offsets far enough aprt to schedule
            not_included : offsets dropped due to overlap and still need to be scheduled
        """
        included = [offsets[0]]
        not_included = []
        for i in range(1, len(offsets)):
            if offsets[i] - included[-1] < sample_len:
                not_included.append(offsets[i])
            else:
                included.append(offsets[i])
        return included, not_included

    def add_loop(self, s, i):
        """
        Append a Sonic Pi live_loop for a single sample
        Breaks the sample's offset list into non-overlapping chunks,
        emits one ring and live_loop per chunk, and uses ADSR parameters
        """
        next_offsets = np.sort(np.unique(np.round(s.offsets,2)))
        start, attack, decay, sustain, release, attack_level, decay_level, sustain_level = self.get_env(s)
        full_path = os.path.abspath(s.file_path)
        self.contents += f"sample{i}='{full_path}'\n"
        loop = 0
        name = s.name.split(".")[0]
        
        while len(next_offsets) > 0:
            included_offsets, next_offsets = self.filter_offsets(next_offsets, s.max_time)
            id = f"_{i}_{name}_{loop}"
            offsets_str = (",").join(map(str, included_offsets)) + "," + str(np.max(s.corr[0]))
            
            self.contents += (
                f"offsets{id} = (ring {offsets_str}) \n"
                f"{id} = 0\n"
                f"live_loop :loop{id} do \n"
                f"\tif offsets{id}[j{id}] > offsets{id}[j{id}-1]\n"
                f"\t\tsleep offsets{id}[j{id}] - offsets{id}[j{id}-1]\n"
                f"\telse\n\t\tsleep offsets{id}[j{id}]\n"
                f"\tend\n"
                f"\tif offsets{id}[j{id}] != offsets{id}[-1]\n"
                f"\t\tsample sample{i}, start: {start}, attack: {attack}, attack_level: {attack_level}, decay: {decay}, decay_level: {decay_level}, sustain: {sustain}, sustain_level: {sustain_level}, release: {release} \n"
                f"\tend\n"
                f"\tj{id} += 1\n"
                f"end\n"
            )
            
            loop += 1
    
    def gen_file(self, dest):
        """
        create single Sonic Pi .rb file
        iterates through samples, calls add_loop for all checked samples
        writes out accumulated self.contents to file in dest
        Args:
            dest (str) : directory path where .rb file created
        """
        for i,s in enumerate(self.samples):
            if s.checked:
                self.add_loop(s, i)
        for i,s in enumerate(self.sonic_samples):
            if s.checked:
                self.add_loop(s, len(self.samples) + i)
        try:
            generated = [name for name in os.listdir(dest) if os.path.isfile(os.path.join(dest, name))]
        except OSError as error:
            print("Error with getting generated tracks:", error)
            generated = []
        generation_count = len(generated)
        file = f"generated_track_{generation_count}.rb"
        # ensure you don't write over previously generated file
        while file in generated:
            generation_count += 1
        file_path = f"{dest}/generated_track_{generation_count}.rb"
        f = open(file_path, "w")
        f.write(self.contents)
        f.close()
        print(file_path)  
    
    def filter_offsets_structured(self, offsets, sample_len):
        """
        Build ring of sleep intervals for a more structured loop
        prepends a 0 to force synchronisation at start 
        breaks into chunks of non-overlapping offsets
        computes sleep times between offsets for the ring

        Args:
            offsets (list): sorted trigger times
            sample_len (float): sample duration
        Returns:
            sleep_times (list): times between successive plays
            not_included (list) : offsets deferred to next loop
        """
        included = [0, offsets[0]]
        not_included = []
        for i in range(1,len(offsets)):
            if offsets[i] - included[-1] < sample_len:
                not_included.append(offsets[i])
            else:
                included.append(offsets[i])
        # compute pairwise differences for the ring
        sleep_times =  [np.round(included[i+1]-included[i],2) for i in range(len(included)-1)]
        return sleep_times, not_included
    
    def add_structured_loop(self, s, i):
        """
        create loop of ring of fixed intervals, plus
        a live_loop that syncs on -1 before restarting

        Args:
            s (Sample_File) : sample instance
            i (int) : index in the sample list
        """
        next_offsets = np.sort(np.unique(np.round(s.offsets,2)))
        start, attack, decay, sustain, release, attack_level, decay_level, sustain_level = self.get_env(s)
        name = s.name.split(".")[0]
        loop = 0
        while len(next_offsets) > 0:
            sleep_times, next_offsets = self.filter_offsets_structured(next_offsets, s.max_time)
            id = f"_{name}_{loop}"
            sleep_times_str = (",").join(map(str, sleep_times)) + ",-1"
            self.contents += f"sleep{id} = (ring {sleep_times_str})\n"
            self.contents += (
                f"live_loop :loop{id} do\n"
                f"\tsleep_time = sleep{id}.tick()\n"
                f"\tif sleep_time ==-1\n"
                f"\t\tsync 'start'\n"
                f"\telse\n"
                f"\t\tsleep sleep_time\n"
                f"\t\tsample samps, {i}, start: {start}, attack: {attack}, attack_level: {attack_level}, decay: {decay}, decay_level: {decay_level}, sustain: {sustain}, sustain_level: {sustain_level}, release: {release}\n"
                f"\tend\n"
                f"end\n"  
            ) 
            loop += 1

    def add_structured_sonic_pi_loop(self, s, i):
        """
        same as add_structured_loop but plays built-in Sonic Pi sample
        Args:
            s (Sonic_Sample_File) : built-in sample instance
            i (int) : index within sonic_samples list
        """
        next_offsets = np.sort(np.unique(np.round(s.offsets,2)))
        start, attack, decay, sustain, release, attack_level, decay_level, sustain_level = self.get_env(s)
        name = s.name.split(".")[0]
        loop = 0
        while len(next_offsets) > 0:
            sleep_times, next_offsets = self.filter_offsets_structured(next_offsets, s.max_time)
            id = f"_{name}_{loop}"
            sleep_times_str = (",").join(map(str, sleep_times)) + ",-1"
            self.contents += f"sleep{id} = (ring {sleep_times_str})\n"
            self.contents += (
                f"live_loop :loop{id} do\n"
                f"\tsleep_time = sleep{id}.tick()\n"
                f"\tif sleep_time ==-1\n"
                f"\t\tsync 'start'\n"
                f"\telse\n"
                f"\t\tsleep sleep_time\n"
                f"\t\tsample {name}, start: {start}, attack: {attack}, attack_level: {attack_level}, decay: {decay}, decay_level: {decay_level}, sustain: {sustain}, sustain_level: {sustain_level}, release: {release}\n"
                f"\tend\n"
                f"end\n"
            )
            loop += 1

    def gen_structured_file(self, dest):
        """
        build a full program that has imporoved structure from gen_file
        - writes samples_folder references and max_time (duration of track)
        - writes :start loop for synchronisation
        - adds loops for each checked sample
        - puts result in a .rb in 'dest'
        """
        # sample folder reference
        self.contents += f"samps = '{self.samples_folder}'\n"
        # global time
        samp = list(self.samples)[0]
        max_time = np.max(samp.corr[0])
        tempo = samp.full_track.tempo
        self.contents += f"use_bpm {tempo}\n"
        self.contents += f"set :max_time, {max_time}\n"
        # loop to synchronise all loops to duration of track
        self.contents += (
            f"live_loop :start do\n"
            f"\tsleep get[:max_time]\n"
            f"\tcue 'start'\n"
            f"end\n"
        )
        for i,s in enumerate(self.samples):
            if s.checked:
                self.add_structured_loop(s, i)
        for i,s in enumerate(self.sonic_samples):
            if s.checked:
                self.add_structured_sonic_pi_loop(s,i)
        # write to dest
        try:
            generated = [name for name in os.listdir(dest) if os.path.isfile(os.path.join(dest, name))]
        except OSError as error:
            print("Error with getting generated tracks:", error)
        generation_count = len(generated)
        file = f"generated_track_{generation_count}.rb"
        while file in generated:
            generation_count += 1
        file_path = f"{dest}/generated_track_{generation_count}.rb"
        f = open(file_path, "w")
        f.write(self.contents)
        f.close()
        print(file_path)

class PloynomialProgramGenerator(ProgramGenerator):
    """
    generator that fits a polynomial to sleep time intervals and uses
    that to define custome 'sleep' function. It then build rings and 
    live loops based on the polynomial model
    """
    def create_sleep_func(self, offsets, samp_no):
        """
        Build Sonic Pi function 'sleep_{samp_no}(x)' that evaluates a 
        polynomial fit to sample's sleep times
        """
        poly = self.fit_offsets(offsets)
        func = f"define :sleep{samp_no} do |x| \n"
        y = "y = "
        print(poly)
        for i,p in enumerate(poly):
            if p != 0:
                y += f"{p}*(x**{len(poly)-(i+1)})"
                if i < len(poly) - 1:
                    y += " + "
        func += f"\t{y}\n\tif y < 0\n\t\ty = y * -1\n\tend\nreturn y\nend"
        return func
    
    def fit_offsets(self, offsets):
        #x = np.array(downbeats)
        offsets = np.insert(offsets,0,0)
        sleep_times = [offsets[i+1]-offsets[i] for i in range(len(offsets)-1)]
        x = [i for i in range(len(sleep_times))]
        x = np.array(x)
        y = np.array(sleep_times)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', np.RankWarning)
            poly = np.polyfit(x,y,max(3, len(sleep_times)))
        return poly
    
    def add_ring(self, s, i):
        name = s.name.split(".")[0]
        offsets = np.sort(np.unique(np.round(s.offsets,2)))
        id = f"_{name}"
        sleep_func = self.create_sleep_func(offsets, id)
        offsets_idx = [f"sleep{id}({i})" for i in range(len(offsets)-1)]
        offsets_idx.append("0")
        offsets_idx = (",").join(map(str, offsets_idx))
        self.contents += f"{sleep_func}\n"
        self.contents += f"sleep_count{id} = (ring {offsets_idx})\n"
    
    def add_live_loop(self, s, i):
        name = s.name.split(".")[0]
        id = f"_{name}"
        start, attack, decay, sustain, release, attack_level, decay_level, sustain_level = self.get_env(s)
        self.contents += f"live_loop :loop{id} do\n\tsleep_time=sleep_count{id}.tick()\n\tif sleep_time == 0\n\t\tsync 'start'\n\telse\n\t\tsleep sleep_time\n\t\tsample samps, {i}, start: {start}, attack: {attack}, attack_level: {attack_level}, decay: {decay}, decay_level: {decay_level}, sustain: {sustain}, sustain_level: {sustain_level}, release: {release}\n\tend\nend\n"
    
    def add_sonic_pi_loop(self, s):
        start, attack, decay, sustain, release, attack_level, decay_level, sustain_level = self.get_env(s)
        name = s.name.split(".")[0]
        id = f"_{name}"
        self.contents += f"live_loop :loop{id} do\n\tsleep_time = sleep_count_{id}.tick()\n\tif sleep_time ==-1\n\t\tsync 'start'\n\telse\n\t\tsleep_{id} sleep_time\n\t\tsample {name}, start: {start}, attack: {attack}, attack_level: {attack_level}, decay: {decay}, decay_level: {decay_level}, sustain: {sustain}, sustain_level: {sustain_level}, release: {release}\n\tend\nend\n"

    def gen_polynomial_file(self, dest):
        self.contents += f"samps = '{self.samples_folder}'\n"
        max_time = np.max(list(self.samples)[0].corr[0])
        self.contents += f"set :max_time, {max_time}\n"
        self.contents += f"live_loop :start do\n\tsleep get[:max_time]\n\tcue 'start'\nend\n"
        for i,s in enumerate(self.samples):
            if s.checked:
                self.add_ring(s,i)
        for i,s in enumerate(self.sonic_samples):
            if s.checked:
                self.add_ring(s, i)
        for i,s in enumerate(self.samples):
            if s.checked:
                self.add_live_loop(s,i)
        for i,s in enumerate(self.sonic_samples):
            if s.checked:
                self.add_sonic_pi_loop(s)
        try:
            generated = [name for name in os.listdir(dest) if os.path.isfile(os.path.join(dest, name))]
        except OSError as error:
            print("Error with getting generated tracks:", error)
        generation_count = len(generated)
        file = f"generated_track_{generation_count}.rb"
        while file in generated:
            generation_count += 1
        file_path = f"{dest}/generated_track_{generation_count}.rb"
        f = open(file_path, "w")
        f.write(self.contents)
        f.close()
        print(file_path)

class DSLProgramGenerator(ProgramGenerator):
    """
    DSL and Rosette synthesiser that builds a Sonic Pi script using
    custom DSL and leverages Rosette for synthesising sleep functions
    """
    def __init__(self, samples, sonic_samples, samples_folder=None):
        super().__init__(samples, sonic_samples, samples_folder)
        self.assertions = []
        self.conds = []
        self.covered = []
        
        self.rqa_det = RQA_Detector()
    
    def synthesise_file(self, dest):
        """
        compose and write a complete Sonic Pi program to dest
            - initialise DSL AST with sample folder, tempo, and downbeat range
            - compute a uniform 'downbeat_time' as the interval between downbeats
            - for each extracted sample
                detect recurring beat patterns
                generate corresponding sleep function via Rosette
                add DSL Sample node that calls that function
            - repeat for built-in Sonic Pi samples
            - wrap both lists of samples in two live_loops 
            ':extracted_samples' and 'sonic_pi_samples' that tick through their sequences
            - transform DSL AST to Sonic Pi code
        
        Args:
            dest (str) : directory where 'generated_track_{n}.rb' saved
        """
        self.contents = []
        self.contents.append(dsl.SampleFolder("samps", self.samples_folder))
        samp = list(self.samples)[0]
        downbeats = samp.full_track.downbeats
        tempo = int(samp.full_track.tempo)
        self.contents.append(dsl.Tempo(tempo))

        # range of downbeat indices and average downbeat interval
        downbeat_count = len(downbeats)
        self.contents.append(dsl.Range("downbeat_count", dsl.Int(0), dsl.Int(downbeat_count), dsl.Int(1)))
        sleep_times = [downbeats[j] - downbeats[j-1] for j in range (1,len(downbeats))]
        downbeat = np.round(np.mean(sleep_times), 2)
        self.contents.append(dsl.Var("downbeat_time", dsl.Float(downbeat)))
        
        # initialise two live loop contents
        live_loop_content = [dsl.Tick("idx", "downbeat_count")]
        sonic_live_loop_content = [dsl.Tick("idx", "downbeat_count")]
        
        # samples extracted from original track: pattern detection, Rosette synthesis
        for i,s in enumerate(self.samples):
            if s.checked:
                detected_patterns = self.rqa_det.sample_pattern_detection(s, downbeats)
                name = s.name.split(".")[0]
                samp_id = f"_{name}"
                #num = name.split("_")[-1]
                sleep_func = self.sleep_function_generation(detected_patterns, samp_id)
                self.contents.append(sleep_func)
                # add DSL Sample that calls new sleep func
                live_loop_content.append(dsl.Sample(f"samps, {i}", dsl.Env(self.get_env(s)), dsl.FunctionCall(f"sleep{samp_id}", dsl.Int("idx"))))

        # built-in Sonic Pi samples: pattern detection, Rosette synthesis
        for i,s in enumerate(self.sonic_samples):
            if s.checked:
                detected_patterns = self.rqa_det.sonic_sample_pattern_detection(s, downbeats)
                name = s.name.split(".")[0]
                samp_id = f"_{name}"
                name = f":{name}"
                num = name.split("_")[-1]
                sleep_func = self.sleep_function_generation(detected_patterns, samp_id)
                self.contents.append(sleep_func)
                sonic_live_loop_content.append(dsl.Sample(name, dsl.Env(self.get_env(s)), dsl.FunctionCall(f"sleep{samp_id}", dsl.Int("idx"))))
        
        # close each loop with sleep of averaged downbeat time
        live_loop_content.append(dsl.Sleep(dsl.Get("downbeat_time")))
        sonic_live_loop_content.append(dsl.Sleep(dsl.Get("downbeat_time")))
        
        # add two DSL live loop nodes
        self.contents.append(dsl.LiveLoop("extracted_samples", live_loop_content))
        self.contents.append(dsl.LiveLoop("sonic_pi_samples", sonic_live_loop_content))
        
        # generate Sonic Pi code and write to new file
        program = dsl.Program(self.contents).to_code()
        try:
            generated = [name for name in os.listdir(dest) if os.path.isfile(os.path.join(dest, name))]
        except OSError as error:
            generated = []
            print("Error with getting generated tracks:", error)
        generation_count = len(generated)
        file = f"generated_track_{generation_count}.rb"
        while file in generated:
            generation_count += 1
            file = f"generated_track_{generation_count}.rb"
        file_path = os.path.join(dest, file)
        f = open(file_path, "w")
        f.write(program)
        f.close()
        print(file_path)
    
    def group_consecutive_beats(self, beat_pattern, target):
        """
        collaps runs of 1s or 0s into (value, length) pairs

        Args:
            beat_pattern : list of binary pattern
            target : target bit value
        Returns:
            list of length of runs of target value and 
            list of corresponding starting indices
        """
        groups = [sum(1 for _ in group) for char, group in itertools.groupby(beat_pattern) if char == target]
        starts = []
        if beat_pattern[0] == target:
            starts.append(0)
        for i in range(1,len(beat_pattern)):
            if beat_pattern[i] == target and beat_pattern[i-1] != target:
                starts.append(i)

        return groups, starts

    def modulus_groups(self, beat_pattern, mod, covered, match):
        """
        group indices by residue class mod N, then pick those classes
        where all uncovered positions share the same bit == match (0 or 1)

        Args:
            beat_pattern (list) : binary sequence
            mod (int) : modulus
            covered (list) : flags to indicate if a position has been covered by an included modulus group
            match (int) : which bit to match (0 or 1)
        Returns:
            dict : mod, res -> bit value
            list or False: updated covered list or False if there were no changes to 
            what indices were covered meaning all indices it had were already covered
            and it is unnecessary to include
        """
        groups = {}
        new_covered = covered.copy()
        for r in range(mod):
            # all indices = r mod 'mod' that remain uncovered
            indices = [i for i in range(r, len(beat_pattern), mod) if not covered[i]]
            if indices:
                # set means that values can't repeat
                # will only be length 1 if it only contains match value
                values = {beat_pattern[i] for i in indices}
                if len(values) == 1:
                    val = values.pop()
                    if val == match:
                        groups[r] = val
                        for i in indices:
                            new_covered[i] = True
        if np.array_equal(new_covered,covered):
            return groups, False
        return groups, new_covered
    
    def pattern_all_same(self, p):
        if 1 not in p:
            # case where all 0s
            return dsl.Return(dsl.Bool("false"))
        elif 0 not in p:
            # case where all 1s
            return dsl.Return(dsl.Bool("true"))
        return None
    
    def pattern_one_hot(self, p):
        if np.count_nonzero(p) == 1:
            # case where there is only one 1
            idx = np.argmax(p)
            assertion_str = f"(assert (<=> (beatmapper-fun x) (bveq x (int32 {idx}))))"
            return self.single_assertion_func(assertion_str, p)
        return None
    
    def pattern_one_zero(self, p):
        if np.count_nonzero(p) == len(p) - 1:
            # case where there is only one 0
            idx = np.argmin(p)
            assertion_str = f"(assert (<=> (not (beatmapper-fun x)) (bveq x (int32 {idx}))))"
            return self.single_assertion_func(assertion_str, p)
        return None
    
    def pattern_contiguous(self, p):
        if len(np.where(np.ediff1d(np.nonzero(p)) != 1)) == 0:
            # case where all ones in a row
            idxs = np.nonzero(p)
            start = idxs[0][0]
            end = idxs[-1][-1]
            assertion_str = f"(assert (<=> (beatmapper-fun x) (and (bvsge x (int32 {start})) (bvsle x (int32 {end})))))"
            return self.single_assertion_func(assertion_str, p)
        if len(np.where(np.ediff1d(np.where(p != 1)) != 1)) == 0:
            # case where all 0s in a row
            idxs = np.where(p != 1)
            start = idxs[0]
            end = idxs[-1]
            assertion_str = f"(assert (<=> (not (beatmapper-fun x)) (and (bvsge x (int32 {start})) (bvsle x (int32 {end})))))"
            return self.single_assertion_func(assertion_str, p)
        return None

    def pattern_even(self, p, match):
        groups, covered_updated = self.modulus_groups(p, 2, self.covered, match)
        print(groups, covered_updated)
        if covered_updated != False:
            self.covered = covered_updated
            for rem, val in groups.items():
                #print(groups)
                if rem == 0:
                    self.conds.append(f"(bveven? x)")
                    self.assertions.append(f"(bveven? x)")
                else:
                    self.conds.append(f"(bvodd? x)")
                    self.assertions.append(f"(bvodd? x)")       

    def pattern_chunks(self, p, match):
        # check for large chunks of match value in a row
        consecutive_len, start_idxs = self.group_consecutive_beats(p, match)
        for i, l in zip(start_idxs, consecutive_len):
            if l > 3:
                if i == 0:
                    self.assertions.append(f"(bvsle x (int32 {i+l}))")
                elif i + l == len(p)-1:
                    self.assertions.append(f"(bvsge x (int32 {i}))")
                else:
                    self.assertions.append(f"(and (bvsge x (int32 {i})) (bvsle x (int32 {i+l})))")
                for x in range(l):
                    self.covered[i + x] = True
    
    def pattern_mod(self, p, match):
        # check for modulus groups ranging up to half the size of the sequence
        for i in range(3, min(32, int(len(p) * 0.5))):
            groups, covered_updated = self.modulus_groups(p, i, self.covered, match)
            if covered_updated != False:
                self.covered = covered_updated
                if i > 9:
                    func = f"bvdiv? (int32 {i})"
                else:
                    # rosette program has predefined functions for mod 2-9
                    func = f"bvdiv{i}?"
                for rem, val in groups.items():
                    if rem > 0:
                        self.conds.append(f"({func} (bvadd x (int32 {i - rem})))")
                        self.assertions.append(f"({func} (bvadd x (int32 {i - rem})))")
                    else:
                        self.conds.append(f"({func} x)")
                        self.assertions.append(f"({func} x)")
    
    def pattern_outliers(self, p, match):
        # generate assertions to address indices with match value not yet covered
        for j in range(len(p)):
            if not self.covered[j]:
                if p[j] == match:
                    self.assertions.append(f"(bveq x (int32 {j}))")

    def single_assertion_func(self, assertion_str, p, pos=True):
        """for a single condition assertion sketch, synthesise a DSL"""
        sketch = f"(define (beatmapper-fun x) (assume (bvsge x (int32 0))) (assume (bvsle x (int32 {len(p)}))) (beat-if x))"
        print(assertion_str)
        print(sketch)
        result = iterative_synth(assertions=assertion_str, upper_bound=len(p)-1, sketch=sketch)
        if result:
            return translate_rosette(result)
        return dsl.Return(dsl.Bool("false"))

    def generate_conditional(self, p):
        """
        Synthesise a Rosette-based conditional that matches exactly the mapping
        from indexes to the corresponding bit (1 or 0) in p

        Returns either:
            dsl.Return(false/true) for all zeros or all ones
            or full Rosette sketch and assertion fed into iterative_synth
        """
        print(p)
        # check for all 0 or all 1
        all_same = self.pattern_all_same(p)
        if all_same is not None:
            return all_same

        p = np.array(p)
        one_hot_pattern = self.pattern_one_hot(p)
        if one_hot_pattern is not None:
            return one_hot_pattern
        one_zero_pattern = self.pattern_one_zero(p)
        if one_zero_pattern is not None:
            return one_zero_pattern
        contiguous_pattern = self.pattern_contiguous(p)
        if contiguous_pattern is not None:
            return contiguous_pattern
        
        return self.synthesise_and_gen(p)
    
    def synthesise_and_gen(self, p):
        """
        build sketch and assertions for more complicated patterns
        """
        # only needs to be valid for indexes within length of p
        sketch = f"(define (beatmapper-fun x) (assume (bvsge x (int32 0))) (assume (bvsle x (int32 {len(p)})))"
        
        # count number of 1s and number of 0s
        count_1 = np.count_nonzero(p)
        count_0 = len(p) - count_1
        # match to bit value with less cases
        if count_0 < count_1:
            match = 0
        else:
            match = 1

        self.assertions = []
        # create list to track that all bits with value match have been covered by the assertions
        self.covered = [False] * len(p)
        # collect modulus division conditions in list, can directly feed these into the sketch for synthesis speed up
        self.conds = []
        # check for if all even or all odd
        self.pattern_even(p, match)
        print(self.assertions)
        # check for large chunks of match value in a row
        self.pattern_chunks(p, match)
        print(self.assertions)
        # check for modulus groups ranging up to half the size of the sequence
        self.pattern_mod(p, match)
        print(self.assertions)
        # check for any match values still left uncovered
        self.pattern_outliers(p, match)
        print(self.assertions)
        
        # manually include if statement that covers included modulus groups to reduce amount of rosette synthesis necessary
        if len(self.conds) > 0:
            if match == 1:
                b = "#t"
            else:
                b = "#f"
            sketch += "(if (or " + (" ").join(self.conds) + f") {b} (beat-if x)))"
        
        # combine assertions
        assertion_str = ("\n").join(self.assertions)
        assertion_str = f"(assert (<=> (or {assertion_str})"
        # if matched to 1 assert that conditions result in true
        # if matched to 0 assert that conditions result in false
        if match == 1:
            assertion_str += " (beatmapper-fun x)))"
        else:
            assertion_str += " (not (beatmapper-fun x))))"
        print(assertion_str)
        # if we have not already, add call to grammar
        if "beat-if" not in sketch:
            sketch += "(beat-if x))"
        print(sketch)
        # synthesise produced sketch
        print(assertion_str)
        print(sketch)
        result = iterative_synth(assertions=assertion_str, upper_bound=len(p)-1, sketch=sketch)
        # on failure return false for all indexes
        if result is None:
            return dsl.Return(dsl.Bool("false"))
        # on successful synthesis translate result to DSL conditional
        return translate_rosette(result)

    def sleep_function_generation(self, patterns, samp_id):
        """
        include multiple conditional bodies into single DSL Function 'sleep{sample_id}'

        Args:
            patterns : list of binary sub-patterns
            samp_id : identifier suffix
        """
        # build a list of split points and per-chunk conditionals
        programs = {}
        total = 0
        splits = []
        for p in patterns:
            total += len(p)
            splits.append(total)
        conditions = [dsl.LT(dsl.Int("x"), dsl.Int(s)) for s in splits[:-1]]
        bodies = []
        for i, p in enumerate(patterns):
            if tuple(p) in programs.keys():
                conditional = programs[tuple(p)]
            else:
                conditional = self.generate_conditional(p)
                programs[tuple(p)] = conditional
            if i > 0:
                conditional = dsl.Program([dsl.NumVar("x", dsl.Sub(dsl.Int("x"), dsl.Int(splits[i]))), conditional])
            bodies.append(conditional)
        # if multiple patterns, wrap using If otherwise single body function
        if len(patterns) > 1:
            func = dsl.Function(f"sleep{samp_id}", [dsl.If(conditions, bodies)], "x")
        else:
            func = dsl.Function(f"sleep{samp_id}", [bodies[0]], "x")
        return func
        
