class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ptr1, ptr2 = 0, -1
        
        for i in range(len(word)):
            if word[i] == ch:
                ptr2 = i
                break
                
        if ptr2 == -1:
            return word

        word = list(word)
        while ptr1 <= ptr2:
            temp = word[ptr1]
            word[ptr1] = word[ptr2]
            word[ptr2] = temp
            ptr1, ptr2 = ptr1 + 1, ptr2 - 1

        return "".join(word)
        