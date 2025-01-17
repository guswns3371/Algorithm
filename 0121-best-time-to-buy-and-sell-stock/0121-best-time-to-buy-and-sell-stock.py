class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices), 1):
            sell = prices[i]
            if buy < sell:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        return profit