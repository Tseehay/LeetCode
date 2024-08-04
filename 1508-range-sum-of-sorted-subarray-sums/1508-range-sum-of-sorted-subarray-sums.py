class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        sum_array = []

        for i in range(len(nums)):
            _sum = 0
            for j in range(i,len(nums)):
                _sum+=nums[j]
                sum_array.append(_sum)

        sum_array.sort()

        result = 0
        for k in range(left - 1, right):
            result = (result + sum_array[k]) % MOD
        
        return result