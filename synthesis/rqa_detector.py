from pyrqa.time_series import TimeSeries
from pyrqa.settings import Settings
from pyrqa.neighbourhood import FixedRadius
from pyrqa.computation import RQAComputation, RPComputation
from pyrqa.metric import EuclideanMetric
from pyrqa.image_generator import ImageGenerator
import ruptures as rpt

import matplotlib.pyplot as plt

import numpy as np

from synthesis.variable_markov_model import VMM

class RQA_Detector:
    """
    pattern detection and recurrence quantification analysis
    for sample and sonic pi patterns
    """

    def sample_pattern_detection(self, sample, downbeats):
        """
        detect rhythmic patterns in sample presence relative to the downbeats

        Args:
            sample: Sample_file instance
            downbeats: list or array of downbeat times
        Returns:
            detected_patterns: list of binary patterns returned by VMM
        """
        sample_offsets = sample.offsets
        binary_encoding = [int(downbeats[i] in sample_offsets) for i in range(len(downbeats))]
        data, recurrence_features, window_pos = self.recurrence_quantification_analysis(binary_encoding, sample.name)
        cluster_patterns, segments, window_labels, window_pos, change_points, beat_classes = self.point_change_analysis(sample.name.split(".")[0], data, recurrence_features, window_pos)
        vmm = VMM(max_order=8)
        detected_patterns = vmm.vmm(binary_encoding, cluster_patterns, segments, window_labels, window_pos, change_points, beat_classes, occurrence_weight=1)
        return detected_patterns
    
    def sonic_sample_pattern_detection(self, sample, beats):
        """
        maps built-in sonic pi sample offsets to closest downbeat and detects patterns
        using same method as extracted samples
        Due to likely low frequency of occurrences, the VMM is fed a high weight relative
        to the pattern length to give preference to playing a sample over not playing a sample
        """
        sample_offsets = sample.offsets
        #set sonic pi samples to be played at closest beat to the offset it was found at
        difference = np.abs(np.subtract.outer(beats, sample_offsets))
        closest_idx = difference.argmin(axis=0)
        offsets_onbeat = np.array(beats)[closest_idx]
        binary_encoding = [int(beats[i] in offsets_onbeat) for i in range(len(beats))]
        data, recurrence_features, window_pos = self.recurrence_quantification_analysis(binary_encoding, sample.name)
        cluster_patterns, segments, window_labels, window_pos, change_points, beat_classes = self.point_change_analysis(sample.name.split(".")[0], data, recurrence_features, window_pos)
        vmm = VMM(max_order=8)
        detected_patterns = vmm.vmm(binary_encoding, cluster_patterns, segments, window_labels, window_pos, change_points, beat_classes, occurrence_weight=2*(len(binary_encoding)))
        return detected_patterns


    def recurrence_quantification_analysis(self, data, name=None):
        """
        sliding-window RQA on binary sequence

        Args:
            data: list or array of binary values
        Returns:
            data : padded binary encoding
            rqa_features : feature vectors from RQA analysis
            window_pos : start indices of windows
        """
        #self.recurrence_plot(data, name)
        window_size = 16
        step_size = 4
        
        # pad short sequences
        if len(data) < window_size:
            pad_len = window_size - len(data)
            data = np.pad(data, (0, pad_len), mode="constant", constant_values=0)

        rqa_features = []
        window_pos = []

        for i in range(0, len(data) - window_size + 1, step_size):
            window = data[i: min(i+window_size, len(data))]
            embedding_dim = 2
            time_delay = 1
            time_series = TimeSeries(window, embedding_dimension=embedding_dim, time_delay=time_delay)

            settings = Settings(
                time_series=time_series,
                neighbourhood=FixedRadius(1.0),
                similarity_measure=EuclideanMetric,
                theiler_corrector=1,
            )

            computation = RQAComputation.create(settings)
            result = computation.run()
            """
            result.recurrence_rate,
            result.determinism,
            result.average_diagonal_line,
            result.longest_diagonal_line,
            result.divergence, 
            result.entropy_diagonal_lines, 
            result.laminarity, 
            result.trapping_time, 
            result.longest_vertical_line,
            result.entropy_vertical_lines,
            result.average_white_vertical_line,
            result.longest_white_vertical_line,
            result.longest_white_vertical_line_inverse,
            result.entropy_white_vertical_lines,
            result.ratio_determinism_recurrence_rate,
            result.ratio_laminarity_determinism
            """
            feature = [
                result.recurrence_rate,
                result.determinism,
                result.average_diagonal_line,
                result.longest_diagonal_line,
                result.divergence, 
                result.entropy_diagonal_lines, 
                result.laminarity, 
                result.trapping_time, 
                result.longest_vertical_line,
                result.entropy_vertical_lines,
                result.average_white_vertical_line,
                result.longest_white_vertical_line,
                result.longest_white_vertical_line_inverse,
                result.entropy_white_vertical_lines,
                result.ratio_determinism_recurrence_rate,
                result.ratio_laminarity_determinism
            ]
            feature = np.nan_to_num(feature, nan=0.0, posinf=np.finfo(np.float32).max, neginf=np.finfo(np.float32).min)

            rqa_features.append(feature)
            window_pos.append(i)
        # normalise features
        rqa_features = np.array(rqa_features)
        global_mean = np.mean(rqa_features, axis=0)
        global_std = (np.std(rqa_features, axis=0))
        epsilon = 1e-10
        rqa_features = (rqa_features - global_mean) / (global_std + epsilon)
        return data, rqa_features, window_pos
    
    def point_change_analysis(self, name, data, rqa_features, window_pos, window_size=16):
        """
        detect change points in recurrence patterns of binary encodings
        using rqa_features as feature vectors

        Args:
            data : padded binary encoding
            rqa_features : feature vectors from RQA analysis
            window_pos : start indices of windows
        Returns:
            class_patterns : dict mapping segment label to sequence
            segments : list of segment sequences
            segment_labels : array of labels per window
            window_pos : start indices of windows
            change_points : list of window indices where change occurs
            beat_classes : array of class label per original data point
        """
        if len(rqa_features) == 1:
            change_points = []
        else:
            # detect change points using PELT
            algo = rpt.Pelt(model="rbf").fit(rqa_features)
            change_points = algo.predict(pen=1)
            if len(window_pos) in change_points:
                change_points.remove(len(window_pos))
        
        # assign segment labels
        num_windows = len(window_pos)
        segment_labels = np.zeros(num_windows, dtype=int)
        current_segment = 0
        prev_cp = 0
        for cp in change_points:
            segment_labels[prev_cp: cp] = current_segment
            current_segment += 1
            prev_cp = cp
        segment_labels[prev_cp:] = current_segment

        # assign each data point to a segment using majority voting
        beat_classes = []
        for b in range(len(data)):
            covering_windows = [i for i,start in enumerate(window_pos) if start <= b < start + window_size-1]
            if len(covering_windows) > 0:
                votes = [segment_labels[i] for i in covering_windows]
                beat_classes.append(np.bincount(votes).argmax())
            else:
                # if not covered default to nearest center
                centers = np.array(window_pos) + window_size//2
                idx = np.argmin(np.abs(centers-b))
                beat_classes.append(segment_labels[idx])
        
        # get group patterns
        segments = []
        classes = np.unique(segment_labels)
        class_patterns = {}
        for i,p in enumerate(classes):
            seg = np.array([data[j] for j in range(len(data)) if beat_classes[j] == p])
            segments.append(seg)
            class_patterns[p] = seg
        
        #self.point_change_plot(name, data, beat_classes, change_points, window_pos)

        beat_classes = np.array(beat_classes)
        return class_patterns, segments, segment_labels, window_pos, change_points, beat_classes
    
    def point_change_plot(self, name, data, beat_classes, change_points, window_pos):
        """
        generate plots showing detected change points
        """
        plt.clf()
        plt.plot(data, label="Binary Data")
        for cp in change_points:
            plt.axvline(x=window_pos[cp], color="red", linestyle="--")
        plt.legend()
        plt.savefig(f'change_point_analysis_plot_{name}.png', dpi=300)
        #plt.show()
        plt.clf()
        # graph showing data labels
        plt.plot(data, label="Binary Data")
        plt.scatter(np.arange(len(data)), data, c=beat_classes, cmap='viridis', s=50, label='Segment labels')
        plt.legend()
        plt.colorbar(label="segment label")
        plt.savefig(f'change_point_analysis_colorbar_{name}.png', dpi=300)
        #plt.show()
    
    def recurrence_plot(self, data, name:str):
        """
        generate recurrence plot 
        """
        if name is None:
            return
        #print("BINARY DATA", data)
        time_delay = 1
        embedding_dim = 2
        time_series = TimeSeries(data, embedding_dimension=embedding_dim, time_delay=time_delay)

        settings = Settings(
            time_series=time_series,
            neighbourhood=FixedRadius(1.0),
            similarity_measure=EuclideanMetric,
            theiler_corrector=1,
        )
        name = name.split(".")[0]
        computation = RPComputation.create(settings)
        result = computation.run()
        ImageGenerator.save_recurrence_plot(result.recurrence_matrix_reverse, f'recurrence_plot_{name}.png')
    
