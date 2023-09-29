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

    def add_end(self, item):
        self.size += 1
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove_index(self, index):
        message = "Successfully removed item: "
        if self.size == 0:
            removed_item = self.head.data
            self.head = None
            self.size -= 1
            print("Succ")
            return

        current = self.head
        count = 0
        while count < index-1:
            current = current.next
        if current is not None and current.next is not None and current.next.next is not None:
            current.next = current.next.next
            print("Successfully removed encapsuled item", current.data)
        else:
            current.next = None
            print("Successfully removed last item", current.data)

    def __str__(self):
        string = str(self.head.data)
        current_next = self.head.next
        count = 0
        while current_next is not None and count < self.size:
            string += f", {current_next.data}"
            current_next = current_next.next
            count += 1
        return string
