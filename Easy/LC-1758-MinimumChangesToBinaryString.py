class Solution:
    def minOperations(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            if i % 2 == 0:
                count += 1 if s[i] == '1' else 0
            if i % 2 != 0:
                count += 1 if s[i] == '0' else 0
                
        return min(count, len(s) - count)