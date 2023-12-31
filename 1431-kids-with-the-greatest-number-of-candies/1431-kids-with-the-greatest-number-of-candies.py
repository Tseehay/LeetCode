class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        n = len(candies)
        result = [False] * n

        for i in range(n):
            if candies[i] + extraCandies >= maxCandies:
                result[i] = True

        return result
        
