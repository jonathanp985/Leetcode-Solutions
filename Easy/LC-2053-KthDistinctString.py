class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)

        for string in arr:
            if freq[string] >= 2:
                continue
            else:
                k -= 1
                
            if k == 0:
                return string

        return ""
