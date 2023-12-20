class Solution:
    def largestOddNumber(self, num: str) -> str:
        for char in range(len(num) - 1, - 1, -1):
          if int(num[char]) % 2 != 0:
           return num[:char + 1]
        return ""
