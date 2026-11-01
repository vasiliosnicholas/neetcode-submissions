class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        chars = {}
        max_length = 0
        for i, c in enumerate(s):
            right = i
            if c in chars and chars[c] >= left:
                left = chars[c] + 1
            chars[c] = i
            max_length = max(max_length, right - left + 1)
        return max_length