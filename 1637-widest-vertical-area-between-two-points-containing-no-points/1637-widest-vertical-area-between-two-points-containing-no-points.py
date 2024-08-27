class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        dif=0
        for i in range(1,len(points)):
            dif=max(dif,points[i][0]-points[i-1][0])
            
        return dif