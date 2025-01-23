class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        profit = 0
        while i < len(prices) and j < len(prices):
            if prices[i] > prices[j]:
                i = j          
            elif prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
            j += 1
        return profit
