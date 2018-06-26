class nestedIterator:
    def __init__(self,nestedList):
        self.stack = []
        self._push_list_to_stack(nestedList)

    def _push_list_to_stack(self,nestedList):
        temp = []
        for i in nestedList:
            temp.append(i)
        while temp:
            self.stack.append(temp.pop())

    def next(self):
        if self.hasnext():
            return self.stack.pop().getInteger()

    def hasnext(self):
        while self.stack and not self.stack[-1].isInteger():
            self._push_list_to_stack(self.stack.pop().getlist)
        return len(self.stack) != 0

