class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
    
        min_val = float('inf')
        mid_val = float('inf')

        for num in nums:
            if num <= min_val:
                min_val = num
            elif num <= mid_val:
                mid_val = num
            else:
                return True

        return False
