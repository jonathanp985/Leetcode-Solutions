# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        cur_sum = 0
        while queue:
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
                if not cur.left.right and not cur.left.left:
                    cur_sum += cur.left.val
            if cur.right:
                queue.append(cur.right)
        return cur_sum