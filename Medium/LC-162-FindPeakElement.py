class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        target = max(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
