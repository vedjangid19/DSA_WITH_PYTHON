""" Queue Implementation using Singly Linked List. """
class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next

class Queue:
    def __init__(self, front=None, rear=None, item_count=0) -> None:
        self.front = front
        self.rear = rear
        self.item_count = item_count

    def is_empty(self):
        return self.front is None and self.rear is None

    def enqueue(self, data):
        if not self.is_empty():
            n = Node(item=data)
            self.rear.next = n
            self.rear = n

            self.item_count += 1
        else:
            n = Node(item=data)
            self.front = n
            self.rear = n

            self.item_count += 1

    def dequeue(self):
        if not self.is_empty():
            if self.item_count == 1:
                self.front = None
                self.rear = None

                self.item_count -= 1
            else:
                self.front = self.front.next

                self.item_count -= 1
        else:
            raise IndexError("Queue is empty.")

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Queue is empty.")

    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Queue is empty.")

    def size(self):
        return self.item_count
    

if __name__ == "__main__":
    queue_obj = Queue()
    queue_obj.enqueue(1)
    queue_obj.enqueue(2)
    queue_obj.enqueue(3)
    queue_obj.enqueue(4)

    print(queue_obj.get_front())
    print(queue_obj.get_rear())
    try:
        queue_obj.dequeue()
    except IndexError as e:
        print(e.args[0])

    print(queue_obj.get_front())
    print(queue_obj.get_rear())
    try:
        queue_obj.dequeue()
    except IndexError as e:
        print(e.args[0])

    print(queue_obj.get_front())
    print(queue_obj.get_rear())
