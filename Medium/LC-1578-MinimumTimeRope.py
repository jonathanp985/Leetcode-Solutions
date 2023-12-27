class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = time = 0

        for r in range(1,len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    time += neededTime[l]
                    l = r
                else:
                    time += neededTime[r]
            else:
                l = r 
                    

        return time
        