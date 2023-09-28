from Node import Node


class MyCollection:
    def __init__(self, item):
        self.size = 1
        self.head = Node(item)

    def add(self, item):
        self.size += 1
        placeholder_node = self.head
        self.head = Node(item)
        self.head.next = placeholder_node

    def __str__(self):
        string = self.head.data
        current_next = self.head.next
        count = 0
        while current_next is not None and count < self.size:
            current_next = current_next.next
            string.append(",", current_next.data)