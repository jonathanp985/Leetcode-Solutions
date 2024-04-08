class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cur = 0
        while students:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                cur = 0
            else:
                cur += 1
                students.append(students.pop(0))

            if cur == len(students):
                return cur
                
        return 0