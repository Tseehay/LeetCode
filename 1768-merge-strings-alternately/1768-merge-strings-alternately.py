class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        w=""
        i=0
        j=0
        while i<len(w1) and j<len(w2):
            w+=w1[i]
            i+=1
            w+=w2[j]
            j+=1
        w+=w1[i:]
        w+=w2[j:]
        return w
        