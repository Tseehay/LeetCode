class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
    
        # Initialize variables
        min_price = float('inf')
        max_profit = 0
        
        # Traverse through the prices array
        for price in prices:
            # Update the minimum price encountered so far
            min_price = min(min_price, price)
            
            # Calculate the potential profit if selling at the current price
            profit = price - min_price
            
            # Update the maximum profit found
            max_profit = max(max_profit, profit)
        return max_profit