# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if cur.right:
                queue.append(cur.right)
            if cur.left:
                queue.append(cur.left)
        return cur.val

                