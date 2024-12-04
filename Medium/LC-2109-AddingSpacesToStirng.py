class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        cur_ind = 0
        for i in range(len(s)):
            if cur_ind < len(spaces) and i == spaces[cur_ind]:
                res += " " + s[i]
                cur_ind += 1
                continue
            res += s[i]
        return res

        