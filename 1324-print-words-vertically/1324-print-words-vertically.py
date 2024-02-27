class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        return [''.join(col).rstrip() for col in zip_longest(*words, fillvalue=' ')]