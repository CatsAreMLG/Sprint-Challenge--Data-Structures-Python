class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage.pop(self.current)
        self.storage.insert(self.current, item)
        if self.current < self.capacity-1:
            self.current += 1
        else:
            self.current = 0

    def get(self):
        return [x for x in self.storage if x is not None]
