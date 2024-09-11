""" Circular Linked List Implementation """

class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next
class CLLIterator:
    def __init__(self, start) -> None:
        self.current = start
        self.count = 0
        self.temp = start

    def __iter__(self):
        return self.current
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        
        if self.current == self.temp and self.count != 0:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current = self.current.next
        return data

class CLL:
    def __init__(self, last=None) -> None:
        self.last = last

    def is_empty(self) -> bool:
        return self.last is None
    
    def insert_at_start(self, data):
        if self.is_empty():
            n = Node(data)
            n.next = n
            self.last = n
        else:
            n = Node(data)
            n.next = self.last.next
            self.last.next = n

    def insert_at_last(self, data):
        if self.is_empty():
            self.insert_at_start(data)
        else:
            n = Node(data)
            n.next = self.last.next
            self.last.next = n
            self.last = n

    def search(self, data):
        if self.is_empty():
            return None
        
        temp = self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next
            
        if temp.item == data:
            return temp
        return None

    def insert_after(self, data, insert_after_data):
        if not self.is_empty():
            temp_ref = self.search(insert_after_data)
            if temp_ref:
                n = Node(data)
                n.next = temp_ref.next
                temp_ref.next = n
                if temp_ref == self.last:
                    self.insert_at_last(data)

    def delete_first(self):
        if not self.is_empty():
            if self.last == self.last.next:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last == self.last.next:
                self.last = None
            else:
                temp = self.last.next
                while temp != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_item(self, data):
        if not self.is_empty():
            if self.last == self.last.next:
                if self.last.item == data:
                    self.delete_last()
            else:
                if self.last.next.item == data:
                    self.delete_first()
                else:
                    temp = self.last.next
                    while temp != self.last:
                        if temp.next == self.last:
                            if self.last.item == data:
                                self.delete_last()
                                break
                        if temp.next.item == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next

    def __iter__(self):
        if self.is_empty():
            return CLLIterator(self.last)
        else:
            return CLLIterator(self.last.next)
    
    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=' ')
                temp = temp.next

            print(temp.item, end=' ')

if __name__ == "__main__":
    cll_obj = CLL()
    cll_obj.insert_at_start(1)
    cll_obj.insert_at_start(2)
    cll_obj.insert_at_start(3)
    cll_obj.insert_at_start(4)
    cll_obj.insert_at_start(5)
    cll_obj.insert_at_last(6)
    cll_obj.insert_at_last(7)

    cll_obj.insert_after(8, 6)

    cll_obj.delete_first()
    cll_obj.delete_last()


    cll_obj.print_list()
    print()
    for i in cll_obj:
         print(i, end=' ')