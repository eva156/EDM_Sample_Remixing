import numpy as np
from collections import defaultdict

class VMM:
    """
    variable-order Markov model and Viterbi decoder
    for binary beat-pattern sequences
    """

    def __init__(self, max_order = 8):
        """
        Args:
            max_order: maximum context length for VMM
        """
        self.max_order = max_order
    
    def vmm(self, binary_encoding, cluster_patterns, segments, window_labels, window_pos, change_points, beat_classes, occurrence_weight=0):
        """
        for each cluster pattern, train VMM on its windows and the template,
        giving more weight to the template then decodes a full-length pattern via Viterbi

        Args: 
            binary_encoding: list containing binary pattern indicating sample presence at each beat
            cluster_patterns: dict label -> template sequence for that cluster
            window_labels: lust of segment labels for each window
            window_pos: list of start indices for each window
            change_points: list of window indices where segment change
        Returns:
            detected_patterns: list of reconstructed binary sequences
        """
        
        # ensure start of sequence point is a change point
        change_points = [0] + change_points
        detected_patterns = []

        for lab, pattern in cluster_patterns.items():
            # collect all windows belonging to cluster
            training = []
            for i,w in enumerate(window_pos):
                if window_labels[i] == lab:
                    training.append(binary_encoding[window_pos[i]:window_pos[i]+16])
            training.append(cluster_patterns[lab])
            counts, initial_counts = self.build_vmm_model(training, occurrence_weight)
            pattern = self.vmm_sequence_viterbi(counts, 8, len(cluster_patterns[lab]), initial_counts)
            detected_patterns.append(pattern)
        return detected_patterns

    def build_vmm_model(self, sequences, occurence_weight, max_order=8):
        """
        build context -> counts maps for next-bit transitions

        Returns:
            counts: dict context -> [number of 0s, number of 1s]
            initial_counts: dict initial context -> weight
        """
        counts = defaultdict(lambda: np.zeros(2))
        initial_counts = defaultdict(lambda: 1)
        start_token = -1

        for j, seq in enumerate(sequences):
            # larger significance given to original sequence in indexes
            # of sequence to be generated
            weight = 10 if j == len(sequences) - 1 else 1

            # pad beginning of sequence
            padded_seq = [start_token] * max_order + list(seq)
            n = len(padded_seq)
            for i in range(1, n):
                for order in range(1, min(max_order, i) + 1):
                    context = tuple(padded_seq[i-order:i])
                    next_state = padded_seq[i]
                    # extra weight if bit is 1 (sample occurrence)
                    if next_state == 1:
                        counts[context][next_state] += occurence_weight
                    counts[context][next_state] += weight
                # track how often each initial bit appears
                if i == max_order:
                    initial_context = tuple(padded_seq[max_order:max_order+1])
                    if 1 in initial_context:
                        initial_counts[initial_context] += occurence_weight
                    initial_counts[initial_context] += weight
        return counts, initial_counts

    def get_probability_distribution(self, counts, context):
        """
        back off from full context dwon to shorter suffices until have nonzero counts
        returns normalised [p0, p1] array
        """
        for order in range(len(context), 0, -1):
            sub_context = context[-order:]
            if sub_context in counts and np.sum(counts[sub_context]) > 0:
                total = np.sum(counts[sub_context])
                return counts[sub_context] / total
            
        return np.array([0,0])

    def vmm_sequence_viterbi(self, counts, max_order, target_length, initial_context_counts):
        """
        standard Viterbi decoding over binary states given
        transition ditributions in 'counts' and start context 
        weights in 'initial_counts'
        """
        # pick most likely initial context
        initial_context = list(initial_context_counts.keys())[np.argmax(list(initial_context_counts.values()))]
        L = len(initial_context)
        # backpointer: at time t, map context -> (prob, previous (context, bit))
        backpointers = {}
        backpointers[L] = {initial_context: (1.0, None)}
        for t in range(L,target_length):
            backpointers[t+1] = {}
            for context, (prob, bp) in backpointers[t].items():
                for s in [0,1]:
                    if len(context) < max_order:
                        new_context = context + (s,)
                    else:
                        new_context = context[1:] + (s,)
                    prob_vec = self.get_probability_distribution(counts, new_context)
                    transition_prob = prob_vec[s]
                    new_prob = prob * transition_prob
                    if new_context not in backpointers[t+1] or new_prob > backpointers[t+1][new_context][0]:
                        backpointers[t+1][new_context] = (new_prob, (context, s))
        # find best final context
        best_context = None
        best_prob = 0
        for context, (prob, bp) in backpointers[target_length].items():
            if prob >= best_prob:
                best_prob = prob
                best_context = context

        # backtrack to recover bits
        sequence = []
        current_context = best_context
        current_time = target_length
        while current_time > L:
            prev_info = backpointers[current_time][current_context][1]
            if prev_info is None:
                break
            prev_context, bit = prev_info
            sequence.append(bit)
            current_context = prev_context
            current_time -= 1
        sequence = list(initial_context) + list(reversed(sequence))
        return sequence