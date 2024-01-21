class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []

        def Traverse(node):
            if not node:
                return
            res.append(node.val if low <= node.val <= high else 0)
            Traverse(node.left)
            Traverse(node.right)

        Traverse(root)
        return sum(res)       