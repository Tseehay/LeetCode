class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        num_count={}
        for num in nums:
            num_count[num]=num_count.get(num,0)+1
            
        num_sort=dict(sorted(num_count.items(),key=lambda x :( x[1],-x[0])))
        l=[]
        for key,count in num_sort.items():
            l+=[key]*count
        
        return l