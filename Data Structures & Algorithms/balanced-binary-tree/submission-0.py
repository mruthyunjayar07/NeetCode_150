# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.heights(root.left)
        right = self.heights(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def heights(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.heights(root.left), self.heights(root.right))
        