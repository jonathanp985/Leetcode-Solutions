class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        order = {5 : 0, 10 : 0, 20 : 0}
        for bill in bills:
            order[bill] += 1

            if bill == 10:
                if order[5] >= 1:
                    order[5] -= 1
                else:
                    return False
            elif bill == 20:
                if order[10] > 0 and order[5] > 0:
                    order[5] -= 1
                    order[10] -= 1

                elif order[5] >= 3:
                    order[5] -= 3
                else:
                    return False
        return True

            