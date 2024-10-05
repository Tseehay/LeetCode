class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        
        l = 0
        for r, c in enumerate(s2):
            cnt[c] -= 1
            while cnt[c] < 0:
                cnt[s2[l]] += 1
                l += 1
            if r - l + 1 == len(s1):
                return True
            
        return False