class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque[str]()
        open = {'{': '}', '(': ')', '[': ']'}
        for c in s:
            if c in open:
                stack.appendleft(open[c])
            elif len(stack) == 0 or stack.popleft() != c:
                return False
        return len(stack) == 0