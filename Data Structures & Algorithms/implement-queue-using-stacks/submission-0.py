class MyQueue:

    def __init__(self):
        self.s_1, self.s_2 = [], []

    def push(self, x: int) -> None:
        self.s_1.append(x)

    def pop(self) -> int:
        if not self.s_2:
            while self.s_1:
                self.s_2.append(self.s_1.pop())
        return self.s_2.pop()

    def peek(self) -> int:
        if not self.s_2:
            while self.s_1:
                self.s_2.append(self.s_1.pop())
        return self.s_2[-1]

    def empty(self) -> bool:
        return not bool(len(self.s_1) + len(self.s_2))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()