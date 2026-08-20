class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_st = prices[0]
        profit = 0
        for i in prices:
            min_st = min(min_st, i)
            profit = max(profit, i - min_st)
        return profit