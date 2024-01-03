class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        n = len(nums)

        for right in range(n):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1

        while left < n:
            nums[left] = 0
            left += 1
