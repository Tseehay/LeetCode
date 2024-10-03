class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0: return 0
        prefix_reminder_dic = {0:-1} 
        reminder = 0
        length = len(nums)
        
        for i, num in enumerate(nums):
            reminder = (reminder + num) % p
            if (reminder - target) % p in prefix_reminder_dic:
                if i - prefix_reminder_dic[(reminder - target) % p] < length:
                    length = i - prefix_reminder_dic[(reminder - target) % p]
            prefix_reminder_dic[reminder] = i
            
        return -1 if length == len(nums) else length    