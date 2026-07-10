class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < cost:
                cost = prices[i]
            elif prices[i] - cost > max_profit:
                max_profit = prices[i] - cost
            
        return max_profit