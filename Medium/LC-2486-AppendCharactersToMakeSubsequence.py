class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(s) and ptr2 < len(t):
            if s[ptr1] == t[ptr2]:
                ptr1, ptr2 = ptr1 + 1, ptr2 + 1
            else:
                ptr1 += 1

        return 0 if ptr2 == len(t) - 1 and s[ptr2] == t[ptr2] else len(t) - ptr2
        