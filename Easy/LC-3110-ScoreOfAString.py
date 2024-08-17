class Solution:
    def scoreOfString(self, s: str) -> int:
        ptr1, ptr2 = 0, 1
        cur_sum = 0
        while ptr2 < len(s):
            cur_sum += abs(ord(s[ptr1]) - ord(s[ptr2]))
            ptr1, ptr2 = ptr1 + 1, ptr2 + 1
        return cur_sum