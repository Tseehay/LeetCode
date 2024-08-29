class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = {}
        count = 0
        for i in answers:
            if i == 0:
                count+=1
            else:
                if i not in d or i == d[i]:
                    d[i] = 0
                    count+=1 + i
                else:
                    d[i] += 1
                    
        return count
