class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell=0
        profit=0
        for i in range(len(prices)-1,-1,-1):
            if prices[i]>sell:
                sell= prices[i]
            else:
                profit = max(profit, sell-prices[i])
        return profit