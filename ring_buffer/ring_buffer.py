class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # remove the oldest value
        self.storage.pop(self.current)
        # replace it with the next value
        self.storage.insert(self.current, item)
        # iterate to next oldest
        if self.current < self.capacity-1:
            self.current += 1
        else:
            self.current = 0

    def get(self):
        # return all not None values
        return [x for x in self.storage if x is not None]
