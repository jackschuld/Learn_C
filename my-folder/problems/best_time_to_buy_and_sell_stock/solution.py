class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapestPrice = float("inf")
        maxReturnProfit = 0
        for price in prices:
            if price > cheapestPrice:
                if price - cheapestPrice > maxReturnProfit:
                    maxReturnProfit = price - cheapestPrice
            else:
                cheapestPrice = price
        return maxReturnProfit
        