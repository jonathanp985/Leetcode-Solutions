class Solution:
    def maxDepth(self, s: str) -> int:
        opened = 0
        cur_max = 0

        for char in s:
            if char == "(":
                opened += 1
                cur_max = max(cur_max, opened)
            elif char == ")": 
                opened -= 1               
        return cur_max