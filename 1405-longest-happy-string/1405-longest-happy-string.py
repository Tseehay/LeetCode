class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count = collections.Counter({'a':a, 'b':b, 'c':c})
        res = ['#']
        while True:
            (a1, _), (a2, _) = count.most_common(2)
            
            if a1 == res[-1] == res[-2]:
                a1 = a2
                
            if not count[a1]:
                break
                
            res.append(a1)
            count[a1] -= 1            
        
        return ''.join(res[1:]) 