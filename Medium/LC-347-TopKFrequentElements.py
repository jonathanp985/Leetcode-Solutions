class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_occ = Counter(nums)
        res = []
        for j in range(k):
            max_freq = 0
            max_freq_num = 0
            for key, value in num_occ.items():
                if value > max_freq:
                    max_freq = value
                    max_freq_num = key
                    
            res.append(max_freq_num)
            num_occ.pop(max_freq_num)

        return res
        
        
        
