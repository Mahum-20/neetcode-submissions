class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxprofit = 0
        minN = prices[0]
        for n in prices:
            profit = n - minN
            maxprofit = max(maxprofit, profit)
            minN = min(minN,n)
        return maxprofit
