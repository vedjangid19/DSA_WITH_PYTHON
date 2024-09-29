""" Queue implementation using list. """

class Queue:
    def __init__(self) -> None:
        self.list = list()
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0
    
    def enqueue(self, data):
        self.list.append(data)
        self.item_count += 1

    def dequeue(self):
        if not self.is_empty():
            self.list.pop(0)
            self.item_count -= 1
        else:
            raise IndexError("Queue is empty.")

    def get_front(self):
        if not self.is_empty():
            return self.list[0]
        else:
            raise IndexError("Queue is empty.")

    def get_rear(self):
        if not self.is_empty():
            return self.list[-1]
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

