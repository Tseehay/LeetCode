class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dSpeed = []
        stack = []
        for i in range(len(position)):
            dSpeed.append((position[i],speed[i]))
        dSpeed = sorted(dSpeed, reverse=True)
        
        for d, speed in dSpeed:
            distance = target-d
            if not stack or (distance/speed)>stack[-1]:
                stack.append(distance/speed)
                
        return len(stack)