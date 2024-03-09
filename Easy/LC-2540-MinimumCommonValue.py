class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums = set(nums1)

        for num in nums2:
            if num in nums:
                return num
        
        return -1