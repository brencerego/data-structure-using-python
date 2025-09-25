class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
    
    def is_empty(self):
        return len(self.queue) == 0  # Corrected to return a boolean value
    
    def size(self):
        print("Size of queue is", len(self.queue))
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        print("Removed", self.queue.pop(0))
    
    def display(self):
        print("Queue", self.queue)
        
q = Queue()        
n = int(input("Enter the number of elements in Queue: "))
for i in range(n):
    q.enqueue(int(input(f"Enter element {i + 1}: ")))
    
q.dequeue()
q.size()
print(q.is_empty())
q.display()

    