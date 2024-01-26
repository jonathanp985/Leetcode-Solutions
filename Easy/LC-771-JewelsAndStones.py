class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        occ = Counter(jewels)
        for char in stones:
            if char in occ:
                res += 1
        return res