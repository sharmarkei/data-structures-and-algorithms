class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class Stack():
    def __init__(self):
        self.top = None
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        current = self.top
        if current:
            self.top = current.next
        else:
            print('Stack is empty.')
    def peek(self):
        if self.top == None:
            return None
        else: 
            current = self.top
            return current.value
    def isEmpty(self):
        return self.top == None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
        else:
            self.front = new_node
        self.rear = new_node
    def dequeue(self):
        current = self.front
        if current != None:
            self.front = current.next
        else:
            print('Queue is empty.')
    def peek(self):
        if self.front == None:
            return None
        current = self.front
        return self.front.value
    def isEmpty(self):
        return self.front == None