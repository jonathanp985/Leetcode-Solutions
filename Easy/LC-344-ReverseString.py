class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s) - 1
        temp = 0
        
        while start < end:
            temp = s[end]
            s[end] = s[start]
            s[start] = temp
            
            start, end, = start + 1, end - 1
            
        return s
    