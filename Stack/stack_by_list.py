"""  stack implementation using list """

class Stack:
    def __init__(self) -> None:
        self.stack_list = []

    def is_empty(self) -> bool:
        return not self.stack_list
    
    def push(self, data):
        self.stack_list.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack_list.pop()
        else:
            raise IndexError("Stack is Empty!")

    def peek(self):
        if not self.is_empty():
            return self.stack_list[-1]
        else:
            raise IndexError("Stack is Empty!")

    def size(self) -> int:
        return len(self.stack_list)


if __name__ == "__main__":
    stack_obj = Stack()
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)
    print("Top element is: ",stack_obj.peek())
    print("removed element is: ",stack_obj.pop())
    print("Top element is: ",stack_obj.peek())


