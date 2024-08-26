class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        res = hi = on = 0
        for l in flips:
            on += 1
            if l>hi:
                hi = l
            if on==hi:
                res+=1
        return res