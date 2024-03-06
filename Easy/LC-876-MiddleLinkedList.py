# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        ptr1, ptr2 = head, head
        
        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        return ptr1