class Node:
    def __init__(self, val):
        self.val = val
        self.min = None
        self.next = None

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            self.head.min = val
        else:
            cur = Node(val)
            cur.min = min(self.head.min, val)
            cur.next = self.head
            self.head = cur
        

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()