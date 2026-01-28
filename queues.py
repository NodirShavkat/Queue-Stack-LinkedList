# Linked List
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, value):
        temp = self.head

        if temp and temp.data == value:
            self.head = temp.next 
            return
        
        while temp and temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next
        
    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end=" > ")
            temp = temp.next
        print("None")


# Stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, new_item):
        self.stack.append(new_item)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
            return
        return -1

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]


# Queue
from collections import deque

class Queue:
    def __init__(self):
        self.deque = deque()

    def enqueue(self, new_item):
        self.deque.append(new_item)

    def dequeu(self):
        if not self.is_empty(): 
            self.deque.popleft()
            return
        return -1
    
    def size(self):
        return len(self.deque)

    def is_empty(self):
        return len(self.deque) == 0
    
    def front(self):
        if not self.is_empty():
            return self.deque[0]
