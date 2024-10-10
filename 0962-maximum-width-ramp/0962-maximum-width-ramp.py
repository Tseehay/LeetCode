class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, num in enumerate(nums):
            if not stack or num < nums[stack[-1]]:
                stack.append(i)

        bestWidth = 0
        for r in range(len(nums) - 1, -1, -1):
            while stack and nums[r] >= nums[stack[-1]]:
                bestWidth = max(bestWidth, r - stack.pop())

        return bestWidth