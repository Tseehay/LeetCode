class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = reduce(or_, nums)
        
        @cache
        def fn(i, mask): 
            if mask == target: return 2**(len(nums)-i)
            if i == len(nums): return 0 
            return fn(i+1, mask | nums[i]) + fn(i+1, mask)
        
        return fn(0, 0)