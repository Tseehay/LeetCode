class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket.values():
                stack.append(char)
            elif char in bracket:
                if not stack or stack.pop() != bracket[char]:
                    return False

        return not stack
            