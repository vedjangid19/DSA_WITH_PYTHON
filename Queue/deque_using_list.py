""" Deque Implemetation using list. """


class Deque:
    def __init__(self) -> None:
        self.list = list()

    def is_empty(self):
        return len(self.list) == 0
    
    def insert_front(self, data):
        self.list.insert(0, data)

    def insert_rear(self, data):
        self.list.append(data)

    def delete_front(self):
        if not self.is_empty():
            self.list.pop(0)
        else:
            raise IndexError("Deque is Empty.")

    def delete_rear(self):
        if not self.is_empty():
            self.list.pop()
        else:
            raise IndexError("Deque is Empty.")

    def get_front(self):
        if not self.is_empty():
            return self.list[0]
        else:
            raise IndexError("Deque is Empty.")

    def get_rear(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            raise IndexError("Deque is Empty.")
    
    def size(self):
        return len(self.list)


if __name__ == "__main__":
    deque_obj = Deque()
    deque_obj.insert_front(1)
    deque_obj.insert_front(2)
    deque_obj.insert_rear(3)
    deque_obj.insert_rear(4)
    # print(deque_obj.list)
    print(f"front: {deque_obj.get_front()}   rear: {deque_obj.get_rear()}")
    deque_obj.delete_front()
    # print(deque_obj.list)
    print(f"front: {deque_obj.get_front()}   rear: {deque_obj.get_rear()}")
    deque_obj.delete_rear()
    # print(deque_obj.list)
    print(f"front: {deque_obj.get_front()}   rear: {deque_obj.get_rear()}")