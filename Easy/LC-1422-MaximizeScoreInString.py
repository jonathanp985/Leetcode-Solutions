class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = 0
        cur_sum = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            cur_sum = max(cur_sum, zeros + ones)
        return cur_sum
        

        