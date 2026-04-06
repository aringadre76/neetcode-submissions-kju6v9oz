class MinStack:

    def __init__(self):
        self.stack = []
        self.sortedStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.sortedStack:
            val = min(val, self.sortedStack[-1])
        else:
            val = val
        self.sortedStack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.sortedStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sortedStack[-1]
        
