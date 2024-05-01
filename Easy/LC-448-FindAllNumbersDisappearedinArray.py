class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(range(1, len(nums) + 1))
        for num in range(len(nums)):
            if nums[num] in set_nums:
                set_nums.remove(nums[num])
        return list(set_nums)