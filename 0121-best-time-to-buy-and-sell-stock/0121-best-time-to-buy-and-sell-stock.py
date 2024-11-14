from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:  # Check for empty list
            return 0
        
        # Initialize variables
        min_price = float('inf')  # Start with a very high min_price
        max_profit = 0  # Start with zero profit
        
        for price in prices:
            # Update min_price if the current price is lower
            if price < min_price:
                min_price = price
            
            # Calculate potential profit and update max_profit
            potential_profit = price - min_price
            if potential_profit > max_profit:
                max_profit = potential_profit
        
        return max_profit