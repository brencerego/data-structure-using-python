class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): # Insert at end
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        print("Deleted:", self.head.data)
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None: # Only one node
            print("Deleted:", self.head.data)
            self.head = None
            return
        prev = self.head
        current = self.head.next
        while current.next:
            prev = current
            current = current.next
        print("Deleted:", current.data)
        prev.next = None

    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 1:
            print("Deleted:", self.head.data)
            self.head = self.head.next
            return
        current = self.head
        prev = None
        count = 1
        while current and count < pos:
            prev = current
            current = current.next
            count += 1
        if current is None:
            print("Invalid position")
            return
        print("Deleted:", current.data)
        prev.next = current.next
        
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example Usage
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.display()

print("deletion at beginning")
sll.delete_beginning() # Delete from beginning
sll.display()

print("deletion at end")
sll.delete_end() # Delete from end
sll.display()

print("deletion at position")
sll.delete_at_position(2) # Delete at position 2
sll.display()