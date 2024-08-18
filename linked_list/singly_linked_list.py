""" Singly Linked List """

class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next


class SLLIterator:
    def __init__(self, start) -> None:
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
    

class SLL:
    def __init__(self, start=None) -> None:
        self.start = start

    def is_empty(self):
        return self.start is None
    
    def search(self, data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return temp
                temp = temp.next
            return None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n
    
    def insert_at_last(self, data):
        n = Node(data)
        
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def insert_after(self, data, after_data):
        ref_node = self.search(after_data)

        if ref_node is not None:
            n = Node(data, ref_node.next)
            ref_node.next = n

    def delete_first(self):
        if not self.is_empty():
            temp = self.start
            self.start = temp.next

    def delete_last(self):
        if not self.is_empty():
            temp = self.start
            if temp.next is None:
                self.start = None
            else:
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None

    def delete_item(self, data):
        if not self.is_empty():
            if self.start.next is None:
                if self.start.item == data:
                    self.start = None
            else:
                temp = self.start
                if temp.item == data:
                    self.start = temp.next
                else:
                    while temp.next is not None:
                        if temp.next.item == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next

    def list_show(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
    
    def __iter__(self):
        return SLLIterator(self.start)



if __name__ == "__main__":

    list_obj = SLL()
    # list_obj.insert_at_start(3)
    list_obj.insert_at_start(1)
    list_obj.insert_at_start(2)
    list_obj.insert_at_last(4)
    # list_obj.insert_after(2.5, 2)
    # list_obj.insert_at_last(5)


    for i in list_obj:
        print(i, end=" ")
    # list_obj.list_show()
    # list_obj.delete_first()
    # list_obj.delete_last()
    list_obj.delete_item(1)
    print()
    # list_obj.list_show()

    for i in list_obj:
        print(i, end=" ")