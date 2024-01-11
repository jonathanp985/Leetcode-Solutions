class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        visited = set()
        for cur in range(len(s)):
            if s[cur] in visited:
                res += 1
                visited = set()
            visited.add(s[cur])
        return res + 1