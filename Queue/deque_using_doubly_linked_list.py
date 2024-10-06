""" Deque Implemetation using Doubly Linked List. """

class Node:
    def __init__(self, prev=None, item=None, next=None) -> None:
        self.prev = prev
        self.item = item
        self.next = next


class Deque:
    def __init__(self, front=None, rear=None) -> None:
        self.front = front
        self.rear = rear
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0
    
    def insert_front(self, data):
        if not self.is_empty():
            n = Node(item=data, next=self.front)
            self.front.prev = n
            self.front = n
            n.prev = self.front

            self.item_count += 1
        else:
            n = Node(item=data)
            self.front = n
            self.rear = n
            n.prev = self.front
            n.next = self.rear

            self.item_count += 1

    def insert_rear(self, data):
        if not self.is_empty():
            n = Node(item=data)
            n.prev = self.rear
            self.rear.next = n
            self.rear = n
            n.next = self.rear

            self.item_count += 1
        else:
            self.insert_front(data=data)
    
    def delete_front(self):
        if not self.is_empty():
            if self.item_count == 1:
                self.front = None
                self.rear = None
                self.item_count -= 1
            else:
                self.front.next.prev = self.front
                self.front = self.front.next

                self.item_count -= 1
        else:
            raise IndexError("Deque is empty.")

    def delete_rear(self):
        if not self.is_empty():
            self.rear.prev.next = self.rear
            self.rear = self.rear.prev

            self.item_count -= 1
        else:
            raise IndexError("Deque is empty.")

    def get_front(self):
        data = self.front.item
        return data

    def get_rear(self):
        data = self.rear.item
        return data

    def size(self):
        return self.item_count
    
    # Deque does not have show item this will be cmt i have written this function for testing pupose
    def show_deque(self):
        if not self.is_empty():
            temp = self.front
            while self.rear != temp:
                print(temp.item, end=' ')
                temp = temp.next

            print(temp.item, end=' ')
            print()

    

if __name__ == "__main__":
    deque_obj = Deque()
    deque_obj.insert_front(1)
    deque_obj.insert_front(2)
    deque_obj.insert_front(3)
    deque_obj.insert_front(4)
    deque_obj.insert_front(5)
    deque_obj.insert_front(6)
    print(f"\nfront: {deque_obj.get_front()}, rear: {deque_obj.get_rear()}, size: {deque_obj.size()}\n")

    deque_obj.insert_rear(2)
    deque_obj.insert_rear(3)
    deque_obj.insert_rear(4)
    deque_obj.insert_rear(5)
    deque_obj.insert_rear(6)

    deque_obj.show_deque()
    print(f"\nfront: {deque_obj.get_front()}, rear: {deque_obj.get_rear()}, size: {deque_obj.size()}\n")

    
    deque_obj.delete_front()

    deque_obj.delete_front()
    deque_obj.delete_front()
    print(f"\nfront: {deque_obj.get_front()}, rear: {deque_obj.get_rear()}, size: {deque_obj.size()}\n")

    deque_obj.show_deque()
    deque_obj.delete_rear()
    deque_obj.show_deque()
    deque_obj.delete_rear()
    deque_obj.show_deque()
    print(f"\nfront: {deque_obj.get_front()}, rear: {deque_obj.get_rear()}, size: {deque_obj.size()}\n")

    deque_obj.delete_rear()
    deque_obj.show_deque()

    print(f"\nfront: {deque_obj.get_front()}, rear: {deque_obj.get_rear()}, size: {deque_obj.size()}\n")

