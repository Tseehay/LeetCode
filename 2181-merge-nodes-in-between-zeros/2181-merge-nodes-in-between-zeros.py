# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        summ = tail = ListNode()
        s = 0
        current = head.next
        
        while current:
            if current.val != 0:
                s += current.val
            else:
                tail.next = ListNode(s)
                tail = tail.next
                s = 0
            current = current.next
            
        return summ.next