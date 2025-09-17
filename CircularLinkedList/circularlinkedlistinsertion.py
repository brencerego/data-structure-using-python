class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
    
    def insert_at_position(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while count < position - 1 and current:
            current = current.next
            count += 1
        if not current:
            print("Position out of range")
            return
        new_node.next = current.next
        current.next = new_node

    def traverse(self):
        if not self.head:
            print("Circular Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("... (Back to Head)")

if __name__ == "__main__": 
    cll = CircularLinkedList()
    cll.insert_at_beginning(3)
    cll.insert_at_beginning(2)
    cll.insert_at_beginning(1)
    print("After inserting at the beginning:")
    cll.traverse()  
    
    cll.append(4)
    print("After appending at the end:")
    cll.traverse()  
    
    cll.insert_at_position(2, 5)
    print("After inserting at position 2:")
    cll.traverse() 
