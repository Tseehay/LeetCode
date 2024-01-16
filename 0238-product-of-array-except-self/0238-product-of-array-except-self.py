class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        answer[0] = 1
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]

        suffix_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer