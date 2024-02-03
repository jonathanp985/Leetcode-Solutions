class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = [[] for i in range((len(nums) // 3))]
        count = 0

        for i in range(len(res)):
            for ele in range(count, count + 3):
                res[i].append(nums[ele])

            if not(res[i][2] - res[i][0] <= k):
                return []
            count += 3
        return res
