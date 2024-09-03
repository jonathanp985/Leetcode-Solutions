class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = 0
        alpha_offset = 96
        for i in s:
            if (ord(i) - alpha_offset) >= 10:
                num *= 100
            else:
                num *= 10
            num += ord(i) - alpha_offset
        
        for i in range(k):
            if num < 10:
                return num
            cur_sum = 0
            while num != 0:
                cur_sum += num % 10
                num //= 10
            num = cur_sum
            
        return num