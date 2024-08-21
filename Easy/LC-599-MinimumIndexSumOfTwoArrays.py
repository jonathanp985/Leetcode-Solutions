class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sums = {}
        res = []
        min_index = float("inf")

        for word in range(len(list1)):
            index_sums[list1[word]] = [word, 0]

        for word in range(len(list2)):
            if list2[word] in index_sums:
                index_sums[list2[word]][1] += 1
                index_sums[list2[word]][0] += word
                min_index = min(min_index, index_sums[list2[word]][0])
        
        for ind in index_sums:
            if index_sums[ind][1] > 0 and index_sums[ind][0] == min_index:
                res.append(ind)

        return res
                