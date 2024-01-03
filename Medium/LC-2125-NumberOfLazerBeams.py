class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if len(bank) < 2:
            return 0
        cur_row , prev_row = 0, 0 
        res = 0

        for i in range(len(bank) - 1):
            if cur_row == 0:
                prev_row = prev_row
            else:
                cur_row, prev_row = 0, 0
            for j in range(len(bank[i])):
                if bank[i][j] == '1':
                    prev_row = prev_row + 1
                if bank[i + 1][j] == '1':
                    cur_row = cur_row + 1
            res = res + (prev_row * cur_row)

        return res
                    