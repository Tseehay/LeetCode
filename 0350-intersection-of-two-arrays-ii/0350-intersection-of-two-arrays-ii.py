class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        inter = []

        for num in count1:
            if num in count2:
                common_count = min(count1[num], count2[num])
                inter.extend([num] * common_count)

        return inter    