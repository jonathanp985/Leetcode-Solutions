class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing = set([i for i in range(1, len(nums)+1)])
        dupe = None 
        for i in nums: 
            if i in missing:
                missing.remove(i)
            else: 
                dupe = i
        return [dupe, missing.pop()]
        

