# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        count = 0
        while stack:
            temp_stack = stack
            stack = []
            for node in temp_stack:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            count += 1
        return count