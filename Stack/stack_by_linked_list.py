"""  stack implementation using linked list. """
class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next

class Stack(list):
    def __init__(self, start=None, item_count=0) -> None:
        self.start = start
        self.item_count = item_count

    def is_empty(self):
        return self.item_count == 0

    def push(self, data):
        if self.is_empty():
            n = Node(item=data)
            self.start = n
            self.item_count += 1
        else:
            n = Node(item=data, next=self.start)
            self.start = n
            self.item_count += 1


    def pop(self):
        if not self.is_empty():
            pop_item = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return pop_item
        else:
            raise IndexError("Stack is Empty!")

    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is Empty!")

    def size(self):
        return self.item_count
    
    # def show_list(self):
    #     temp = self.start

    #     while temp.next:
    #         print(temp.item, end=' ')
    #         temp = temp.next
    #     print(temp.item, end=' ')
        
        

if __name__ == "__main__":
    stack_obj = Stack()
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)
    # stack_obj.show_list()
    print(f"size of list: {stack_obj.size()}")

    print("Top element is: ",stack_obj.peek())
    stack_obj.pop()
    print(f"size of list: {stack_obj.size()}")
    # stack_obj.show_list()
    print("removed element is: ",stack_obj.pop())
    # stack_obj.show_list()

    print("Top element is: ",stack_obj.peek())
    print(f"size of list: {stack_obj.size()}")


