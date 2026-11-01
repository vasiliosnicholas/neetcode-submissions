class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy, sell, = 0, 0
        for i in range(1, len(prices)):
            if prices[i] < prices[buy]:
                buy = i
                sell = i
            elif prices[i] > prices[sell]:
                sell = i
                profit = max(profit, prices[sell] - prices[buy])
        return profit
                