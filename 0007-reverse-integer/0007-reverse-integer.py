class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = abs(x)

        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        if  rev > 2**31 - 1:
            return 0
        return -rev if negative else rev 