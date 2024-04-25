class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)
        while(l<r):
            md=(l+r)//2
            if target==nums[md]:
                return md
            elif target > nums[md]:
                l= md+1
            else:
                r=md
        return l
            
                