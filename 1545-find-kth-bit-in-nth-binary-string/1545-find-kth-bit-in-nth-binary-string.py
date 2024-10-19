class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'  # base case for S_1
        length = (1 << n) - 1  # length of S_n is 2^n - 1
        mid = length // 2 + 1  # middle position
        
        if k == mid:
            return '1'  # the middle bit is always '1'
        elif k < mid:
            return self.findKthBit(n - 1, k)  # first half
        else:
            return '1' if self.findKthBit(n - 1, length - k + 1) == '0' else '0'  # second half (reverse-inverted)