class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        pacer = -sys.maxsize
        for p, s in sorted(zip(position, speed), reverse=True): 
            v = (target - p)  / s
            if v > pacer:
                pacer = v 
                ans += 1
        return ans 