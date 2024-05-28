class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        dd, dv = abs(dividend), abs(divisor)
        res = 0
        while dd >= dv:
            tmp, mul = dv, 1
            while dd >= (tmp << 1):
                tmp <<= 1
                mul <<= 1
            dd -= tmp
            res += mul

        if  (dividend < 0) ^ (divisor < 0):
            res = -res
        
        return res