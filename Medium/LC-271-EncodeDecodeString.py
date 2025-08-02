class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + ":" + word 
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        char = 0
        while char < len(s):
            cur = ""
            cur_number = ""
            while s[char] != ":":
                cur_number += s[char]
                char += 1

            for i in range(char + 1,  int(cur_number) + char + 1):
                cur += s[i]
            char += int(cur_number) + 1
            res.append(cur)

        return res
