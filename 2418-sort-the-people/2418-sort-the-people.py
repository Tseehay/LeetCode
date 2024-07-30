class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic={}
        for i in range(len(names)):
            dic.update({heights[i]:names[i]})
            dicSort=dict(sorted(dic.items()))
        l=[]
        for val in dicSort.values():
            l.append(val)
        
        return(l[::-1])
            
       