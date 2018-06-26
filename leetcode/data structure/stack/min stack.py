class minStack:
    def __init__(self):
        self.items = []
        self.mins = []

    def push(self,number):
        self.items.append(number)
        if len(self.mins) == 0:
            self.mins.append(number)
        else:
            self.mins.append(min(self.mins[-1],number))

    def pop(self):
        if len(self.items) == 0:
            return None
        self.mins.pop()
        return self.items.pop()

    def min(self):
        return self.mins[-1]

min_stack = minStack()
min_stack.push(1)
min_stack.push(2)
min_stack.push(0.1)
print(min_stack.min())