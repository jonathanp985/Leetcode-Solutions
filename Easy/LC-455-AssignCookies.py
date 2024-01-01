class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        g_ptr, s_ptr = len(g) - 1, len(s) - 1
        res = 0
        while g_ptr >= 0 and s_ptr >= 0:
            if s[s_ptr] >= g[g_ptr]:
                g_ptr, s_ptr = g_ptr - 1, s_ptr - 1
                res += 1
            else:
                g_ptr -= 1
        return res

