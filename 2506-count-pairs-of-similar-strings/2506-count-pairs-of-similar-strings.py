class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = {}
        c = 0
        for word in words:
            sorted_chars = ''.join(sorted(set(word)))
            if sorted_chars in res:
                res[sorted_chars] += 1
            else:
                res[sorted_chars] = 1
        
        for count in res.values():
            if count > 1:
                c += (count * (count - 1)) // 2
        
        return c