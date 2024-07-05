# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first = prev_critical = -1
        min_dist = float("inf")
        index = 1
        prev, curr = head, head.next

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - prev_critical)
                prev_critical = index
            prev, curr = curr, curr.next
            index += 1

        if min_dist == float("inf"):
            return [-1, -1]

        return [min_dist, prev_critical - first]

        