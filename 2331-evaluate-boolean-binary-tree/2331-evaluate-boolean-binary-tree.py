# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
            if root is None:
                return False

            if root.left is None and root.right is None:
                return bool(root.val)

            left_val = self.evaluateTree(root.left)
            right_val = self.evaluateTree(root.right)

            return (root.val == 2 and (left_val or right_val)) or (root.val == 3 and (left_val and right_val))