class Solution:

    def __init__(self, nums: List[int]):
        self.num_list = nums
        self.const = nums

    def reset(self) -> List[int]:
        num_list = self.const
        return num_list

    def shuffle(self) -> List[int]:
        res = [0] * len(self.num_list)
        picked = set()

        for i in range(len(self.num_list)):
            cur_pick = random.randint(0, len(self.num_list) - 1)

            while cur_pick in picked:
                cur_pick = random.randint(0, len(self.num_list) - 1)

            picked.add(cur_pick)
            res[i] = self.num_list[cur_pick] 

        self.num_list = res
        return self.num_list


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()