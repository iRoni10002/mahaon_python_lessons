class MyQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, item, x):
        item[::-1]
        item.append(x)
        item[::-1]
        return item

    def dequeue(self, item):
        return item[len(item) - 1:len(item)]

    def size(self, item):
        return len(item)

    def isEmpty(self, item):
        if len(item) > 0:
            return True
        else:
            return False

kazax = MyQueue
print(kazax.enqueue(kazax, [1, 2, 3, 4, 5], 3))
print(kazax.dequeue(kazax, [1, 2, 3, 4, 5]))
print(kazax.isEmpty(kazax, [1, 2, 3, 4, 5]))
