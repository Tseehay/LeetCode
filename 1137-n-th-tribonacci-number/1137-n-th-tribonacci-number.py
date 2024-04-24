class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n==1 and n==2:
            return 1
        elif n==0:
            return 0
        a, b, c = 0, 1, 1

        for i in range(3, n + 1):
            next_value = a + b + c
            a = b
            b = c
            c = next_value

        return c
