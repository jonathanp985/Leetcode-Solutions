class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_sum = 0
        res = 0
        for i in range(len(gain)):
            cur_sum = cur_sum + gain[i]
            res = max(cur_sum, res)
        return res