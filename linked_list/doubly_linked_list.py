""" Doubly Linked List """

class Node:
    def __init__(self, prev=None, item=None, next=None) -> None:
        self.prev = prev
        self.item = item
        self.next = next

class DLLIterator:
    def __init__(self, start) -> None:
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        
        data = self.current.item
        self.current = self.current.next
        return data

class DLL:
    def __init__(self, start=None) -> None:
        self.start = start

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self, data):
        if self.is_empty():
            n = Node(item=data)
            self.start = n
        else:
            n = Node(item=data, next=self.start)
            self.start.prev = n
            self.start = n

    def insert_at_last(self, data):
        if self.is_empty():
            n = Node(item=data)
            self.start = n
        else:
            n = Node(item=data)
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n.prev = temp
            temp.next = n
    
    def insert_after(self, data, search_data):
        if not self.is_empty():
            ref_node = self.search(search_data=search_data)
            if ref_node is not None:
                if ref_node.next is None:
                    n = Node(prev=ref_node, item=data)
                    ref_node.next = n
                else:
                    n = Node(prev=ref_node, item=data, next=ref_node.next)
                    ref_node.next.prev = n
                    ref_node.next = n

    def delete_first(self):
        if not self.is_empty():
            if self.start.next == None:
                self.start = None
            else:
                self.start.next.prev = None
                self.start = self.start.next

    def delete_last(self):
        if not self.is_empty():
            if self.start.next == None:
                self.start = None
            else:
                temp = self.start
                while temp.next.next is not None:
                    temp = temp.next
                
                temp.next = None
    
    def delete_item(self, delete_data):
        if not self.is_empty():
            if self.start.next is None:
                if self.start.item == delete_data:
                    self.start = None
            else:
                temp_ref = self.search(search_data=delete_data)
                if temp_ref:
                    if temp_ref.prev is None:
                        temp_ref.next.prev = None
                        self.start = temp_ref.next
                    elif temp_ref.next is None:
                        temp_ref.prev.next = None
                    else:
                        temp_ref.prev.next = temp_ref.next
                        temp_ref.next.prev = temp_ref.prev

                

    def search(self, search_data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == search_data:
                    return temp
                temp = temp.next

    
    
    def __iter__(self):
        return DLLIterator(self.start)




if __name__ == "__main__":
    dll_list_obj = DLL()
    dll_list_obj.insert_at_start(1)
    # dll_list_obj.insert_at_start(2)
    # dll_list_obj.insert_at_start(3)


    # dll_list_obj.insert_at_last(4)

    # dll_list_obj.insert_after(data=5, search_data=1)

    # dll_list_obj.delete_first()
    # dll_list_obj.delete_last()
    dll_list_obj.delete_item(delete_data=1)

    for i in dll_list_obj:
        print(i, end=" ")