class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l=len(arr)
        c=0
        for i in range(l):
            if (arr[i])%2 != 0:
                c+=1
                if c==3:
                    return True
            else:
                c=0
        return False
            
            