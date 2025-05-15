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
        #change_points = [0] + change_points
        detected_patterns = []

        for lab, pattern in cluster_patterns.items():
            # collect all windows belonging to cluster
            training = []
            for i,w in enumerate(window_pos):
                if window_labels[i] == lab:
                    training.append(binary_encoding[window_pos[i]:window_pos[i]+16])
            original = cluster_patterns[lab]
            training.append(original)
            # if only one instance of sample return now as likely want this singular occurrence
            # or if already all zeros
            print(original)
            if sum(original) <= 1:
                detected_patterns.append(original)
            else:
                counts, initial_counts = self.build_vmm_model(training, occurrence_weight)
                pattern = self.vmm_sequence_viterbi(counts, 8, len(original), initial_counts)
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
        initial_counts = defaultdict(lambda: 0)
        start_token = -1

        for j, seq in enumerate(sequences):
            # larger significance given to original sequence in indexes
            # of sequence to be generated
            weight = 16 if j == len(sequences) - 1 else 1
            padded_seq = seq
            n = len(padded_seq)

            # record initial context
            initial_context = tuple(padded_seq[:2])
            initial_counts[initial_context] += weight
            for i in range(max_order, n):
                for order in range(1, min(max_order, i) + 1):
                    context = tuple(padded_seq[i-order:i])
                    next_state = padded_seq[i]
                    # extra weight if bit is 1 (sample occurrence)
                    if next_state == 1:
                        counts[context][next_state] += occurence_weight
                    counts[context][next_state] += weight
        #normaise initial counts into probabilities
        total = sum(initial_counts.values())
        initial_counts = {ctx: count/total for ctx, count in initial_counts.items()}
        return counts, initial_counts

    def get_probability_distribution(self, counts, context, epsilon=1e-5):
        """
        back off from full context down to shorter suffices until have nonzero counts
        returns normalised [p0, p1] array
        if no context matches, return uniform 0.5
        """
        for order in range(len(context), 0, -1):
            sub_context = context[-order:]
            if sub_context in counts:
                count0, count1 = counts[context]
                #total = np.sum(counts[sub_context])
                total = count0 + count1
                if total > 0:
                    prob_vector = np.array([count0/total, count1/total])
                    for i, p in enumerate(prob_vector):
                        prob_vector[i] = max(epsilon, p)
                    return prob_vector
            
        return np.array([0.5, 0.5])

    def vmm_sequence_viterbi(self, counts, max_order, target_length, initial_context_counts):
        """
        standard Viterbi decoding over binary states given
        transition ditributions in 'counts' and start context 
        weights in 'initial_counts'
        """
        L = max_order
        # backpointer: at time t, map context -> (prob, previous context, bit)
        backpointers = {max_order: {
            context: (np.log(max(p, 1e-5)), None, None)
            for context, p in initial_context_counts.items()
        }}
        for t in range(max_order, target_length + max_order):
            backpointers[t+1] = {}
            for context, (prob, bp, b) in backpointers[t].items():
                for s in [0,1]:
                    new_context = context[1:] + (s,)
                    transition_prob = self.get_probability_distribution(counts, new_context)
                    new_prob = prob + np.log(transition_prob[s])
                    if new_context not in backpointers[t+1] or new_prob > backpointers[t+1][new_context][0]:
                        backpointers[t+1][new_context] = (new_prob, context, s)
        # find best final context
        final = target_length + L
        best_context, _ = max(backpointers[final].items(), key=lambda x: x[1][0])

        # backtrack to recover bits
        sequence = []
        current_context = best_context
        current_time = final
        while current_time > L:
            prob, prev_context, bit = backpointers[current_time][current_context]
            sequence.append(bit)
            current_context = prev_context
            current_time -= 1
        sequence = list(reversed(sequence))
        return sequence