class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        target_sum = skill[0] + skill[-1]
        
        total_chemistry = 0
        n = len(skill)
        
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != target_sum:
                return -1 
            total_chemistry += skill[i] * skill[n - 1 - i]
        
        return total_chemistry  