class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        c=s=1
        for i in range(time):
            c+=s
            if c==n or c==1:
                s*=-1
        return c
            
            