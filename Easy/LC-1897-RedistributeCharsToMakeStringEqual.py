class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hash_map = {}
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in hash_map:
                    hash_map[words[i][j]] = 0
                hash_map[words[i][j]] += 1

        for i in hash_map:
            if hash_map[i] % len(words) != 0:
                return False
        return True
        