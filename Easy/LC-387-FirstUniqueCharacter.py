class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for char in range(len(s)):
            if s[char] not in count:
                count[s[char]] = [char, 0]
            count[s[char]][1] += 1

        for char in count:
            if count[char][1] == 1:
                return count[char][0]
                
        return -1
    
    