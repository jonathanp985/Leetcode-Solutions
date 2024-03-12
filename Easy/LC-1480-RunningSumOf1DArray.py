class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curSum = 0
        res = []
        for num in range(len(nums)):
            curSum += nums[num]
            res.append(curSum)
        return res
    