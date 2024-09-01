class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != n * m:
            return []

        res = [[]]
        row = 0
        for i in range(len(original)):
            res[row].append(original[i])

            if (i + 1) % n == 0 and i != len(original) - 1:
                res.append([])
                row += 1

        return res 
        