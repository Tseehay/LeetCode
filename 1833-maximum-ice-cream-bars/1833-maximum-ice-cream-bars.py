class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        for i in range(len(costs)):
            if coins>=costs[i]:
                coins-=costs[i]
                count+=1
        
        return count
            
                