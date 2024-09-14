"""  stack implementation using list inheritance. """

class Stack(list):
    def is_empty(self):
        return len(self) == 0

    def push(self, data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty!")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty!")

    def size(self):
        return len(self)
    
    def insert(self, index, data):
        raise AttributeError("No attribute found insert in stack!")




if __name__ == "__main__":
    stack_obj = Stack()
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)
    print("Top element is: ",stack_obj.peek())
    print("removed element is: ",stack_obj.pop())
    print("Top element is: ",stack_obj.peek())
    stack_obj.insert(1, 5)
