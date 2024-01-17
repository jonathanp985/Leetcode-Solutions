class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_occ = defaultdict(int)
        for num in arr:
            if num not in arr:
                num_occ[num] = 0
            num_occ[num] += 1

        for i in num_occ:
            for j in num_occ:
                if i == j:
                    continue
                if num_occ[i] == num_occ[j]:
                    return False
            
        return True