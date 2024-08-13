class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        l,r=0,sum(nums)
        n=len(nums)
        ans=[0]
        m=r
        for i in range(n):
            if nums[i]==0:
                l+=1
            else:
                r-=1
            s=l+r
            if s==m:
                ans.append(i+1)
            elif s>m:
                ans=[]
                ans.append(i+1)
                m=s
        return ans                 