# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0, list1)
        cur, end = list1, list2
        cnt = 0
        while cur:
            if cnt == a - 1:
                ptr1 = cur
            elif cnt == b + 1:
                ptr2 = cur
            cnt += 1
            cur = cur.next

        while end.next:
            end = end.next

        ptr1.next, end.next = list2, ptr2

        return dummy.next