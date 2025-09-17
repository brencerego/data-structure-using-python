class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Delete at beginning
    def delete_at_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # Delete at end
    def delete_at_end(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None
        temp=None

    # Delete at given position (1-based index)
    def delete_at_position(self, pos):
        if self.head is None:
            print("empty list.")
            return
        temp = self.head
        count = 1
        while temp and count < pos:
            temp = temp.next
            count += 1
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        temp=None

    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

# Main driver code
dll = DoublyLinkedList()
# Inserting elements
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
dll.display()

# Deletion at beginning
print("deleting at beginning:")
dll.delete_at_beginning()
dll.display()

# Deletion at end
print("deleting at end:")
dll.delete_at_end()
dll.display()

# Deletion at position 2
print("deleting at position 2:")
dll.delete_at_position(2)
dll.display()
