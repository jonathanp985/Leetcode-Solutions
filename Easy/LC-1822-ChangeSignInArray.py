class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negs = 0
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                negs += 1
        if not negs % 2:
            return 1
        else:
            return -1