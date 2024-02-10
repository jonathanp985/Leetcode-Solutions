class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        cur_max = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l, r = r, r + 1
            else:
                cur_max = max(cur_max, prices[r] - prices[l])
                r = r + 1
        return cur_max