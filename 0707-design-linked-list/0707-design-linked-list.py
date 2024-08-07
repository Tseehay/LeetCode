class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        
        curr = self.head

        while index != 0:
            curr = curr.next
            index -= 1
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        if not self.head:
            self.head = new_node
        else:
            curr = self.head

            while curr.next:
                curr = curr.next
            
            curr.next = new_node

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        
        elif index == 0:
            self.addAtHead(val)
        
        elif index == self.length:
            self.addAtTail(val)
        
        else:
            curr = self.head

            while index - 1 != 0:
                curr = curr.next
                index -= 1
            
            new_node = ListNode(val)

            new_node.next = curr.next
            curr.next = new_node

            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        
        elif index == 0:
            temp = self.head
            self.head = self.head.next
            del temp
        
        else:
            curr = self.head
            while index - 1 != 0:
                curr = curr.next
                index -= 1
            
            temp = curr.next

            curr.next = temp.next
            del temp

        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
