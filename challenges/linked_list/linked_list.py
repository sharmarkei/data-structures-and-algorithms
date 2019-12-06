class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def insert(self, desired_location):
        new_node = node(desired_location)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def includes(self, data):
        if not self.head:
            return False
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def to_list(self):
        elems = " "
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems += " " + str(cur_node.data)

        print(elems)


my_list = linked_list()
my_list.to_list()

my_list.insert(1)
my_list.insert(2)
my_list.insert("HELLO")
print(my_list.includes("HELLO"))
my_list.to_list()
