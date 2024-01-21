class Solution:
    def average(self, n: List[int]) -> float:
        sum=0
        for i in n:
            sum+=i
        ma=max(n)
        mi=min(n) 
        y=len(n)
        return ((sum-(ma+mi))/(y-2))