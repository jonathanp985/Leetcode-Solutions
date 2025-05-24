class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for word in range(len(words)):
            if x in words[word]:
                res.append(word)
        return res
