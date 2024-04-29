class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_iter = iter(t)
        return all(char in t_iter for char in s)