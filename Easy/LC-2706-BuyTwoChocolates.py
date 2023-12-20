class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        arr = sorted(prices)
        money -= arr[0] + arr[1]
        return money if money >= 0 else money + (arr[0] + arr[1])
    
