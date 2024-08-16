class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_value = arrays[0][0]
        max_value = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            max_distance = max(max_distance, abs(arrays[i][-1] - min_value), abs(max_value - arrays[i][0]))
            min_value = min(min_value, arrays[i][0])
            max_value = max(max_value, arrays[i][-1])

        return max_distance
