class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_one = "qwertyuiopQWERTYUIOP"
        row_two = "asdfghjklASDFGHJKL"
        row_three = "zxcvbnmZXCVBNM"

        res = []

        for word in words:
            f = 0
            if word[0] in row_one:
                for char in word:
                    if char not in row_one:
                        f = 1
                        break
                
            elif word[0] in row_two:
                for char in word:
                    if char not in row_two:
                        f = 1
                        break
            else:
                for char in word:
                    if char not in row_three:
                        f = 1
                        break
            if f == 0:
                res.append(word)
        return res