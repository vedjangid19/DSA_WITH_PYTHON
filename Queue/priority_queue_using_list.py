""" Priority Queue using List. """

class PriorityQueue:
    def __init__(self) -> None:
        self.list = list()

    def push(self, data, priority):
        index = 0
        while index < len(self.list) and self.list[index][1] <= priority:
            index += 1

        self.list.insert(index, (data, priority))

    def pop(self):
        if not self.is_empty():
            data = self.list.pop(0)
            return data[0]
        else:
            raise IndexError("Priority Queue is empty.")

    def is_empty(self):
        return len(self.list) == 0
    
    def size(self):
        return len(self.list)
    

if __name__ == "__main__":
    priority_queue_obj = PriorityQueue()
    priority_queue_obj.push(data=1, priority=2)
    priority_queue_obj.push(data=2, priority=1)
    priority_queue_obj.push(data=3, priority=5)
    priority_queue_obj.push(data=4, priority=2)
    priority_queue_obj.push(data=5, priority=3)
    priority_queue_obj.push(data=6, priority=2)
    print(priority_queue_obj.list)
    print(priority_queue_obj.pop())
    print(priority_queue_obj.pop())

    # priority_queue_obj.push(data=6, priority=2)

