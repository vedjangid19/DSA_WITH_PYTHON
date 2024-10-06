""" Priority Queue implementation using linked list. """

class Node:
    def __init__(self, item=None, priority=0, next=None) -> None:
        self.item = item
        self.priority = priority
        self.next = next

class PriorityQueue:
    def __init__(self, start=None, item_count=0) -> None:
        self.start = start
        self.item_count = item_count
    
    def push(self, data, priority):
        n = Node(item=data, priority=priority)

        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n

        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next

            n.next = temp.next
            temp.next = n

        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next

            self.item_count -= 1
            return data
        else:
            raise IndexError("Priority Queue is empty.")

    def is_empty(self):
        return self.item_count == 0
    
    def size(self):
        return self.item_count
    
    def show_list(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != None:
                print(temp.item, end=' ')
                temp = temp.next

            print(temp.item, end=' ')
            print()
    

if __name__ == "__main__":
    priority_queue_obj = PriorityQueue()

    priority_queue_obj.push(data=1, priority=2)
    priority_queue_obj.show_list()

    priority_queue_obj.push(data=2, priority=1)
    priority_queue_obj.show_list()

    priority_queue_obj.push(data=3, priority=5)
    priority_queue_obj.show_list()

    priority_queue_obj.push(data=4, priority=2)
    priority_queue_obj.show_list()
    
    priority_queue_obj.push(data=5, priority=3)
    priority_queue_obj.show_list()

    priority_queue_obj.push(data=6, priority=2)

    priority_queue_obj.show_list()

    print(priority_queue_obj.pop())
    print(priority_queue_obj.pop())
    priority_queue_obj.show_list()

