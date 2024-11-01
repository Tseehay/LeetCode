class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for ch in s: 
            if len(stack) > 1 and stack[-2] == stack[-1] == ch: continue 
            stack.append(ch)
        return "".join(stack)