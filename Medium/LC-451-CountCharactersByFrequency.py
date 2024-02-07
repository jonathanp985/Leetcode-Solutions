class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        cur = []
        res = ""
        for i in count:
            heapq.heappush(cur, (-count[i], i))
        
        for i in range(len(cur)):
            temp = heapq.heappop(cur)
            res += temp[1] * -temp[0]
            
        return res