class Stack:
    def __init__(self):
        self.items = []
    
    # Add an element to the stack
    def push(self, item):
        self.items.append(item)
    
    # Remove and return the top element from the stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Or raise an exception
    
    # Return the top element without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None  # Or raise an exception
    
    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0
    
    # Return the size of the stack
    def size(self):
        return len(self.items)
    
    # For debugging: display the stack
    def display(self):
        print(self.items)

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack contents after pushing:", stack.items)  # [10, 20, 30]
print("Top element:", stack.peek())  # 30
print("Popped element:", stack.pop())  # 30
print("Stack after popping:", stack.items)  # [10, 20]
print("Is stack empty?", stack.is_empty())  # False
print("Stack size:", stack.size())  # 2
