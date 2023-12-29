class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score = max(nums)
        for op in range(1, k):
            score += max(nums) + op
        return score
