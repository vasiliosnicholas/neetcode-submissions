class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        hash_by_freqs: dict[(list[str], list[int]), list[str]] = {}
        for s in strs: # n strings,  Θ(n + m)
            char_freq: dict[str, int] = {} # O(26) == O(1) space.
            for c in s: # m chars in longest string, Θ(m)
                char_freq[c] = char_freq.setdefault(c, 0) + 1

            hashable_dict = frozenset(char_freq.items())
            if hashable_dict not in hash_by_freqs:
                hash_by_freqs[hashable_dict] = [s]
            else:
                hash_by_freqs[hashable_dict].append(s)
        return list(hash_by_freqs.values()) #O(n) space