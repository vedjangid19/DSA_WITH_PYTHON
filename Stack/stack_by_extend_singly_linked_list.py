"""   stack extending using linked list.  """

from singly_linked_list import SLL


class Stack(SLL):
    def __init__(self, start=None, item_count=0) -> None:
        super().__init__(start)
        self.item_count = item_count

    def is_empty(self):
        return self.item_count == 0
    
    def push(self, data):
        self.insert_at_start(data)
        self.item_count += 1            

    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count -= 1
        else:
            raise IndexError("Stack is Empty!")

    def peek(self):
        if not self.is_empty():
            data = self.start.item
            return data
        else:
            raise IndexError("Stack is Empty!")

    def size(self):
        return self.item_count
    
    
if __name__ == "__main__":
    stack_obj = Stack()

    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)

    stack_obj.list_show()
    print(f"stack size is : {stack_obj.size()}")
    stack_obj.pop()
    stack_obj.list_show()

    print(f"stack size is : {stack_obj.size()}")
    print(f"stack peek element is: {stack_obj.peek()}")

