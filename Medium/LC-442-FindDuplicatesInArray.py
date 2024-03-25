class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        freq = Counter(nums)
        for num in freq:
            if freq[num] >= 2:
                res.append(num)
        return res