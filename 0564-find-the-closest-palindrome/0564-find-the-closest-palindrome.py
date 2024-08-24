class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def generatePalindrome(prefix, isEven):
            s = str(prefix)
            return int(s + s[-2 :: -1] if not isEven else s + s[::-1])

        if len(n) == 1:
            return str(int(n) - 1)
        
        num = int(n)
        length = len(n)
        prefix = int(n[:(length + 1) // 2])

        candidates = {
            10**(length - 1) - 1,
            10**length + 1,
            generatePalindrome(prefix - 1, length % 2 == 0),
            generatePalindrome(prefix, length % 2 == 0),
            generatePalindrome(prefix + 1, length % 2 == 0)
        }

        candidates.discard(num)
        return str(min(candidates, key=lambda x: (abs(x - num), x)))