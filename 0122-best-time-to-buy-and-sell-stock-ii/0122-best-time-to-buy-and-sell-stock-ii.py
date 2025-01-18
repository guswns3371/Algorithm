class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        profit = 0

        buy = prices[0]
        for i in range(1, len(prices), 1):
            sell = prices[i]
            
            if sell <= prices[i - 1]:
                buy = sell
                total_profit += profit
                profit = 0
            elif buy < sell:
                profit = max(profit, sell - buy)

        return total_profit + profit

        