class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front, back = 0, len(numbers) - 1

        while numbers[front] + numbers[back] != target:
            cur_sum = numbers[front] + numbers[back]
            if cur_sum > target:
                back -= 1
            else:
                front += 1

        return [front + 1, back + 1]
        