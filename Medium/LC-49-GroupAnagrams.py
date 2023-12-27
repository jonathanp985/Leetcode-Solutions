class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        res = []

        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in hash_map:
                hash_map["".join(sorted(strs[i]))].append(strs[i])
            else:
                hash_map["".join(sorted(strs[i]))] = [strs[i]]
                
        for i in hash_map:
            res.append(hash_map[i])
        return res





        