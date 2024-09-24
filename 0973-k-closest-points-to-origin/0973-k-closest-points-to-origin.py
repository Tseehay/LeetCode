class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        for x, y in points:
            d= (x**2)+(y**2)
            minheap.append([d,x,y])
            
        heapq.heapify(minheap)
        res=[]
        while k > 0 :
            d,x,y=heapq.heappop(minheap)
            res.append([x,y])
            k-=1
        return res
        