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
        currentNext = self.head.next
        count = 0
        while currentNext is not None and count < self.size:
            string.append(currentNext.data)
            

