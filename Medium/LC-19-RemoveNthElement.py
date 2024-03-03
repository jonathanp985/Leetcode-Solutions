# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get length of list
        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next

        if not head.next or length - n == 0:
            return head.next

        # Index of node minus 1
        ind = length - n - 1
        cur = head
        for i in range(ind):
            cur = cur.next
        cur.next = cur.next.next if cur.next else None

        return head
        
    