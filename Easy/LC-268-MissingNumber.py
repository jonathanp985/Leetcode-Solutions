class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = (len(nums) * (len(nums) + 1)) // 2
        return expected_sum - sum(nums)