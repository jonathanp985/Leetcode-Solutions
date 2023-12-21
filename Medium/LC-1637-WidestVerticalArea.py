class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ptr1, ptr2 = 0, 1
        cur_max = 0

        points = sorted(points)

        while ptr2 < len(points):
            cur_max = max(cur_max, points[ptr2][0] - points[ptr1][0])
            ptr1 += 1
            ptr2 += 1
        return cur_max
    
