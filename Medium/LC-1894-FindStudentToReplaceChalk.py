class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        mod = k % sum(chalk)
        if mod == 0:
            return 0

        cur_sum = 0
        for i in range(len(chalk)):
            cur_sum += chalk[i]
            if cur_sum > mod:
                return i
                
        return 