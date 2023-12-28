class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str((int("".join([str(n) for n in digits])) + 1))))
    