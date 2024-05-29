class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_count = {}
        operations = 0

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        for num in nums:
            complement = k - num
            if num_count.get(num, 0) > 0 and num_count.get(complement, 0) > 0:
                if num == complement and num_count[num] < 2:
                    continue
                operations += 1
                num_count[num] -= 1
                num_count[complement] -= 1

        return operations