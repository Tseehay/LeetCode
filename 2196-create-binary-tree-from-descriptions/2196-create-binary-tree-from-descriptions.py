# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children,parentTochildren=set(),{}
        
        for parent,child,isLeft in descriptions:
            children.add(child)
            if parent not in parentTochildren:
                parentTochildren[parent]=[]
                
            parentTochildren[parent].append((child, isLeft))
            
        root=TreeNode(next(iter(set(parent for parent,i,j in descriptions)- children)))
        queue=deque([root])
        
        while queue:
            parent=queue.popleft()
            for childvalue,isLeft in parentTochildren.get(parent.val, []):
                child= TreeNode(childvalue)
                queue.append(child)
                if isLeft:
                    parent.left=child
                else:
                    parent.right=child
        
        return root
            
        