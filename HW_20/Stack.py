class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Error: Stack is empty. Cannot pop from an empty stack.")
            return None

    def is_empty(self):
        return len(self.stack) == 0
    

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Original Stack:")
print(stack.stack)

popped_element = stack.pop()
print("\nPopped Element:", popped_element)

print("\nStack after popping:")
print(stack.stack)