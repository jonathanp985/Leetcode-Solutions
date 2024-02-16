class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        cur_max = 0
        res = 0
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
            cur_max = max(freq[num], cur_max)
        
        for num in freq:
            if freq[num] == cur_max:
                res += freq[num]
        return res
