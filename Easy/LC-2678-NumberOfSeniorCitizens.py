class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num_old = 0
        for passenger in details:
            if int(passenger[11:13]) > 60:
                num_old += 1
        return num_old