class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = str([c for c in s if c.isalnum()])
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
            i += 1
            j -= 1
        return True