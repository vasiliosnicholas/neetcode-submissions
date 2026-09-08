class Solution:
    @staticmethod
    def _update(memo: dict[str, int], key: str):
        memo[key] = memo.setdefault(key, 0) + 1

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_memo = {}
        t_memo = {}
        for s_c, t_c in zip(s, t):
            Solution._update(s_memo, s_c)
            Solution._update(t_memo, t_c)
        return s_memo == t_memo