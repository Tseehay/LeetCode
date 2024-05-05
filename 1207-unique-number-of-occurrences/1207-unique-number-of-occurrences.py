class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(map(arr.count, arr))) == len(set(arr))