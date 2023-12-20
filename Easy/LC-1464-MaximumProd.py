class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest, secondLargest = 0, 0
        for i in range(len(nums)):
            if nums[i] > largest:
                secondLargest = largest
                largest = nums[i]
            else:
                secondLargest = max(nums[i], secondLargest)
        return (largest - 1) * (secondLargest - 1)
        