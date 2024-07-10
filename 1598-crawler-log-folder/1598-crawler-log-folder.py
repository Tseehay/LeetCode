class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        
        for log in logs:
            if log=="../" and stack:
                stack.pop()
            elif (log=="./") or (log=="../" and not stack):
                continue
            else:
                stack.append(log)
        return len(stack)
    
    
                
                
                        