from ..linked_list.singly_linked_list import SLL
# from singly_linked_list import SLL


class Stack:
    def __init__(self) -> None:
        self.SLL = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.SLL.is_empty()
    
    def push(self, data):
        self.SLL.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.SLL.start.item
            self.SLL.delete_first()
            self.item_count -= 1
            return data
        return None

    def peek(self):
        if not self.is_empty():
            return self.SLL.start.item
        return None

    def size(self):
        return self.item_count
    
    def show_list(self):
        self.SLL.list_show()
    

if __name__ == "__main__":
    stack_obj = Stack()

    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)

    stack_obj.show_list()
    print(f"stack size is : {stack_obj.size()}")
    stack_obj.pop()
    stack_obj.show_list()

    print(f"stack size is : {stack_obj.size()}")
    print(f"stack peek element is: {stack_obj.peek()}")
        
            
