class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powers = []
        power = 1
        while power <= n:
            powers.append(power)
            power *= 3
        def backtrack(n, index):
            if n == 0:
                return True
            if n < 0 or index >= len(powers):
                return False
            return backtrack(n - powers[index], index + 1) or backtrack(n, index + 1)

        return backtrack(n, 0)