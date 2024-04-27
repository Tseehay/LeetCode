class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        matches = {}
        for i in range(n):
            matches.setdefault(ring[i], []).append(i)
        
        pos_cost = [(0, 0)]
        for ch in key:
            pos_cost_curr = []
            for curr_pos in matches[ch]:
                curr_cost = float('inf')
                for pos, cost in pos_cost:
                    clkwise_trans_cost = abs(pos - curr_pos)
                    temp_cost = cost + min(clkwise_trans_cost, n - clkwise_trans_cost)
                    curr_cost = min(curr_cost, temp_cost)
                pos_cost_curr.append((curr_pos, curr_cost))
            pos_cost = pos_cost_curr
        
        min_cost = float('inf')
        for pos, cost in pos_cost:
            min_cost = min(min_cost, cost)
        
        return min_cost + len(key)