class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        if nums[left] == nums[right]:
            return -1
            
        while left < right:
            if abs(nums[left]) == nums[right]:
                return abs(nums[right])
            if abs(nums[left]) > nums[right]:
                left += 1
            if abs(nums[left]) < nums[right]:
                right -= 1
        return -1 