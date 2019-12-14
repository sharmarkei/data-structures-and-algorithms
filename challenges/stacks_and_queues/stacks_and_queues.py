class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, top):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        temp = self.top
        if temp.next != None:
            self.top = new temp.next
            temp.next = None
            return temp
        else:
            return 'I'll have you know I graduated'

    def peek(self):
        current = self.top
        return current.data

    def isEmpty(self):
        return self.top == None

class Queue:

    def __init__(self):
      self.front = None)
      pass

    def enqueue(self):
        pass

    def dequeue(self):
        pass

    def peek(self):
        pass

    def isEmpty(self):
        pass
