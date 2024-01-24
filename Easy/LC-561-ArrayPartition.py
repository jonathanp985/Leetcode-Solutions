class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ptr1, ptr2 = len(nums) - 1, len(nums) - 2
        nums = sorted(nums)
        cur_sum = 0
        
        while ptr1 > 0:
            cur_sum += min(nums[ptr1], nums[ptr2])
            ptr1, ptr2 = ptr1 - 2, ptr2 - 2
        return cur_sum