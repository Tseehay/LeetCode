"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        li=[]
        if root is None:
            return
        def nary(node):
            if node is None:
                return
            for child in node.children:
                nary(child)
            li.append(node.val)
               
        nary(root)
        return li
        