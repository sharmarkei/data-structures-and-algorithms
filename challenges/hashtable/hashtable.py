init_size = 50

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.capacity = init_size
        self.size = 0
        self.bucket = [None]*self.capacity
    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum


    def contains(self, key):
        index = self.hash(key)
        node = self.bucket[index]
        if node == None:
            return False
        else:
            return True

    def get(self, key):
        index = self.hash(key)
        node = self.bucket[index]
        while node != None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def add(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.bucket[index]
        if node is None:
            self.bucket[index] = Node(key, value)
            return
        prev = node 
        while node is not None:
            prev = node 
            node = node.next
        prev.next = Node(key, value)