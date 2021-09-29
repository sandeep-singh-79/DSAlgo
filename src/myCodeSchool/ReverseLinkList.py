# Given pointer to the head node of a linked list, the task is to reverse the linked list. We need to reverse the list by changing the links between nodes.

# Examples: 

# Input: Head of following linked list 
# 1->2->3->4->NULL 
# Output: Linked list should be changed to, 
# 4->3->2->1->NULL

# Input: Head of following linked list 
# 1->2->3->4->5->NULL 
# Output: Linked list should be changed to, 
# 5->4->3->2->1->NULL

# Input: NULL 
# Output: NULL

# Input: 1->NULL 
# Output: 1->NULL

class Node(object):
    def __init__(self, value):
        self.next = None
        self.data = value

class ListIterator:
    def __init__(self, node):
        self.current = node
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.current is None:
            raise StopIteration()

        result = self.current.data
        self.current = self.current.next

        return result


class LinkedList:
    def __init__(self, value):
        self.head: Node = Node(value)
        self.tail = self.head
        self.length: int = 1
    
    def prepend(self, value:object):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1
    
    def append(self, value: object):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def insert(self, value: object, index: int):
        '''
        The method inserts a new node with the given value at the provided index. The indexation of the list items starts with 1.
        So, if the user wants to insert an element at the first position then: LinkedList.insert(10, 1).
        If user wants to insert at the end of the list then: LinkedList(10, LinkedList.length)

        Parameters:\n
        ------------------------------------------------------------------------
        name: value
        description: value to be inserted in the list
        type: object

        name: index
        description: the index at which the value is to be inserted. The index of the list starts from 1. So if the user wants to insert the new value at the beginning, he should use the index 1 and so on.
        type: int
        '''
        if index > self.length: raise IndexError("index cannot be greater than length of the list")
        if index == 1: self.prepend(value)
        if index == self.length: self.append(value)
        
        # traverse to the appropriate index element
        node: Node = Node(value)
        priorNode: Node = self.__traverseTo(index-1)
        nextNode: Node = priorNode.next
        priorNode.next = node
        node.next = nextNode
        self.length += 1


    def __traverseTo(self, index:int) -> Node:
        if index > self.length: raise IndexError("index cannot be greater than length of the list")

        node:Node = self.head
        for idx in range(0, index):
            node = node.next
        return node
    
    def search(self, valueToSearch: object) -> Node:
        node = self.head.next
        while node.next != None:
            if node.data == valueToSearch: return node
            node = node.next
        return None

    def printList(self):
        return
    
    def removeFirst(self) -> Node:
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node
    
    def removeLast(self) -> Node:
        if self.length == 1:
            self.removeFirst()
        node = self.__traverseTo((self.length - 1))
        node.next = None
        self.tail = node
        self.length -= 1
        return node
    

    def removeAt(self, index: int) -> Node:
        if index > self.length: raise IndexError("index cannot be greater than length of the list")
        if index == 1: return self.removeFirst()

        priorNode = self.__traverseTo(index - 1)
        nodeToRemove = priorNode.next
        priorNode.next = nodeToRemove.next
        nodeToRemove.next = None
        self.length -= 1
        
        return nodeToRemove
