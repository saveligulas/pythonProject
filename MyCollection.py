from Node import Node


class MyCollection:
    def __init__(self):
        self.size = 1
        self.head = None

    def add(self, item):
        self.size += 1
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def __str__(self):
        string = str(self.head.data)
        current_next = self.head.next
        count = 0
        while current_next is not None and count < self.size:
            string += f", {current_next.data}"
            current_next = current_next.next
            count += 1
        return string
