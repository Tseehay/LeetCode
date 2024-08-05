class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        tran=[[strs[j][i] for j in range(len(strs))]for i in range(len(strs[0]))]
        
        count=0
        for c in tran:
            for i in range(len(c)):
                try:
                    if ord(c[i])>ord(c[i+1]):
                        count+=1
                        break
                except Exception:
                    pass
                
        return(count)
                   