class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hash_map = {}
        res = 0
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 0
            hash_map[nums[i]] += 1

        for num in hash_map:
            if hash_map[num] < 2:
                return -1
            res += hash_map[num] // 3
            if hash_map[num] % 3:
                res += 1
        return res
        