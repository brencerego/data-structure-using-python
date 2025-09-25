class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return f"Popped: {self.stack.pop()}"
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return f"Top: {self.stack[-1]}"
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print("Stack from top to bottom:", self.stack[::-1])
            
    def even(self):
        return "\n".join(f"even index is: {self.stack[i]}" 
            for i in range(0, len(self.stack), 2))

    def odd(self):
        return "\n".join(f"odd index is: {self.stack[i]}" 
            for i in range(1, len(self.stack), 2))

s = Stack()
num_items = int(input("How many numbers to push into stack: "))
for _ in range(num_items):
    item = int(input("Enter a number: "))
    s.push(item)

s.display()

print(s.peek())
print(s.pop())
s.display()

print(s.peek())
print(s.even())
print(s.odd())
print(s.is_empty())
s.display()


s.display() 