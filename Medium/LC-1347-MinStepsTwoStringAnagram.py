class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = {}
        t_freq = {}
        res_diff = 0

        for char in s:
            if char not in s_freq:
                s_freq[char] = 0
            s_freq[char] += 1

        for char in t:
            if char not in t_freq:
                t_freq[char] = 0
            t_freq[char] += 1

        for i in s_freq:

            if i in t_freq and t_freq[i] < s_freq[i]:
                res_diff += abs(s_freq[i] - t_freq[i])

            if i not in t_freq:
                res_diff += s_freq[i]
                
        return res_diff
        
        
        
        