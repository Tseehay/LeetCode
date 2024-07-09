class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t=0
        wait=0
        l=len(customers)
        
        for x,y in customers:
            t=max(t,x)
            wait+=t-x+y
            t+=y
        
        return wait/l