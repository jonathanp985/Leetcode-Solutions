# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next == None:
                return False
                
        ptr1 = head
        ptr2 = head.next
        
        while ptr1 != ptr2:
            if not ptr2 or ptr2.next == None:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        return True