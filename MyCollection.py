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
        message = "Successfully removed item:"
        if self.size == 0:
            removed_item = self.head.data
            self.head = None
            self.size -= 1
            print(message, removed_item)
            return

        if 0 > index > self.size:
            print("Index is out of bounds")
            return

        current = self.head
        count = 0
        while count < index-1:
            count += 1
            current = current.next

        removed_item = current.next.data
        self.size -= 1

        if current.next.next is not None:
            current.next = current.next.next
            print(message, removed_item)
        else:
            current.next = None
            print(message, removed_item)

    def remove_object(self, object):
        current = self.head
        count = 0
        while current is not None:
            if current.data == object:
                self.remove_index(count)
                print("Successfully removed item:", current.data)
                break
            current = current.next
            count += 1

    def __str__(self):
        string = str(self.head.data)
        current_next = self.head.next
        count = 0
        while current_next is not None and count < self.size:
            string += f", {current_next.data}"
            current_next = current_next.next
            count += 1
        return string
