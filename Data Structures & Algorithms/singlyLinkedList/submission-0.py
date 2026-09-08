class Node:
    def __init__(self, val: int, next: Node = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __iter__(self):
        self.iter = self.head
        return self
    
    def __next__(self):
        curr = self.iter
        if self.iter:
            self.iter = self.iter.next
        else:
            raise StopIteration
        return curr.val

    def _get(self, index: int) -> Node:
        count = 0
        iterator = self.head
        while count < index and iterator:
            iterator = iterator.next
            count += 1
        return iterator
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        return self._get(index).val
        
    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        if self.length == 0:
            self.tail = self.head
        self.length += 1

    def insertTail(self, val: int) -> None:
        if self.length == 0:
            self.insertHead(val)
        else:
            new_tail = Node(val)
            self.tail.next = new_tail
            self.tail = new_tail
            self.length += 1
        

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.head = self.head.next
        else:
            prev = self._get(index - 1)
            prev.next = prev.next.next
            if index == self.length - 1:
                self.tail = prev
        self.length -= 1 
        return True
        
    def getValues(self) -> List[int]:
        return [i for i in self]