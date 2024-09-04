# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li=[]
        def indr(node):
            if node:
                indr(node.left)
                li.append(node.val)
                indr(node.right)
                
        indr(root)
        return li