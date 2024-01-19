class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_min = float("inf")
        cur = 0
        left = 0
        for i in range(len(nums)):
            cur += nums[i]
            while cur >= target:
                cur_min = min(cur_min, i + 1 - left)
                cur -= nums[left]
                left += 1
        return cur_min if cur_min != float("inf") else 0
        