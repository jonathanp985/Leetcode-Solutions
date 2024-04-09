class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds = 0
        bound = tickets[k]

        for i in range(len(tickets)):
            if i <= k:
                seconds += min(tickets[i], bound)
            else:
                seconds += min(tickets[i], bound - 1)
            

        return seconds 