""" Circular Doubly Linked List Implementation """

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class CDLLIterator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.current == None:
            raise StopIteration

        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1

        data = self.current.item
        self.current = self.current.next
        return data

class CDLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        if self.is_empty():
            n = Node(item=data)
            n.prev = n
            n.next = n
            self.start = n

        else:
            n = Node(item=data)
            n.prev = self.start.prev
            n.next = self.start

            self.start.prev.next = n
            self.start.prev = n
            self.start = n

    def insert_at_last(self, data):
        if self.is_empty():
            self.insert_at_start(data)
        else:
            n = Node(item=data)
            n.prev = self.start.prev
            n.next = self.start

            self.start.prev.next = n
            self.start.prev = n

    def insert_at_after(self, data, insert_after):
        if not self.is_empty():
            temp_ref = self.search(insert_after)
            if temp_ref:
                if temp_ref == self.start.prev:
                    self.insert_at_last(data)
                else:
                    n = Node(item=data)
                    n.prev = temp_ref.next
                    n.next = temp_ref.next
                    temp_ref.next.prev = n
                    temp_ref.next = n

    def delete_first(self):
        if not self.is_empty():
            if self.start == self.start.next:
                self.start= None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next


    def delete_last(self):
        if not self.is_empty():
            if self.start == self.start.next:
                self.start= None
            else:
                self.start.prev = self.start.prev.prev
                self.start.prev.next = self.start


    def delete_item(self, data):
        if not self.is_empty():
            if self.start == self.start.next: # if list has only one node
                if self.start.item == data:
                    self.start = None
            else:
                temp = self.start
                while temp.next != self.start:
                    if temp == self.start:

                        if temp.item == data:
                            self.start.next.prev = self.start.prev
                            self.start.prev.next = self.start.next
                            self.start = self.start.next
                            temp = temp.next
                            break
                    else:
                        if temp.item == data:
                            print("x", temp.item)
                            temp.prev.next = temp.next
                            temp.next.prev = temp.prev
                            temp = temp.next
                            break
                    temp = temp.next

                if temp.item == data:
                    # pass
                    self.delete_last()




    def search(self, data):
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                if temp.item == data:
                    return temp
                temp = temp.next
            if temp.item == data:
                return temp

            return None

    def print_list(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                print(temp.item, end=" ")
                temp = temp.next
            print(temp.item, end=" ")

    def __iter__(self):
        return CDLLIterator(self.start)

if __name__ == "__main__":
    cdll_obj = CDLL()
    cdll_obj.insert_at_start(1)
    cdll_obj.insert_at_start(2)
    cdll_obj.insert_at_start(4)
    cdll_obj.insert_at_start(3)
    # cdll_obj.insert_at_last(4)
    # cdll_obj.insert_at_last(5)
    # # a = cdll_obj.search(13)
    # # print("a: ", a)
    # cdll_obj.insert_at_after(31, 5)

    # cdll_obj.delete_first()
    cdll_obj.print_list()
    # cdll_obj.delete_last()
    print("\n-----------\n")
    cdll_obj.delete_item(1)
    cdll_obj.print_list()
    print("\n-----------\n")
    for i in cdll_obj:
        print(i, end=" ")