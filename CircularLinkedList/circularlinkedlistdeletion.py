class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete_at_beginning(self):
        if not self.head:
            print("Circular Linked List is empty")
            return
        
        if self.head.next == self.head:
            self.head = None
            return

        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = self.head.next
        self.head = self.head.next
        
    def delete_at_position(self, position):
        if not self.head:
            print("Circular Linked List is empty")
            return
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return
        current = self.head
        count = 0
        while count < position - 1 and current.next != self.head:
            current = current.next
            count += 1
        if count < position - 1:
            print("Position out of range")
            return
        current.next = current.next.next
    
    def display(self):
        if not self.head:
            print("Circular Linked List is empty")
            return
        
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("... (circular)")

if __name__ == "__main__": 
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    
    print("Circular Linked List before deletion:")
    cll.display()
    
    print("\nAfter deleting the first node:")
    cll.delete_at_beginning()
    cll.display()

    print("\nAfter deleting node at position 1:")
    cll.delete_at_position(1)
    cll.display()
    
    print("\nAfter deleting the first node again:")
    cll.delete_at_beginning()
    cll.display()
