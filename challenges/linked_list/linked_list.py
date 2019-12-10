class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        list_str = ""
        current = self.head
        while current:
            list_str += str(current.value)
            if current.next:
                list_str += ", "
            current = current.next
        return list_str

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def append(self, value):
        current = self.head
        while current:
            if current.next == None:
                node = Node(value)
                current.next = node
                return
            current = current.next

    def insert_before(self, value, new_value):
        node = Node(new_value)

        if self.head and self.head.value == value:
            node.next = self.head
            self.head = node
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                node.next = current.next
                current.next = node
                break
            current = current.next

    def insert_after(self, value, new_value):
        current = self.head
        while current:
            if current.value == value:
                node = Node(new_value)
                node.next = current.next
                current.next = node
                break
            current = current.next

    def kth_from_end(self,n):
        current = self.head
        future = current

        for i in range(0,n):
            try:
                future = future.next
            except AttributeError:
                raise AttributeError('Not in the list')
        while future.next:
            future = future.next
            current = current.next
        return current.value
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None