# http://www.lintcode.com/zh-cn/problem/min-stack/
class MinStack:

    def __init__(self):
        self.datas = []
        self.mins = []
        self.index = -1

    def push(self, number):
        numArr = [number]
        self.datas[self.index + 1:self.index + 2] = numArr

        if self.index == -1 or self.mins[self.index] > number:
            self.mins[self.index + 1:self.index + 2] = numArr
        else:
            self.mins[self.index + 1:self.index + 2] = [self.mins[self.index]]
        self.index += 1

    def pop(self):
        if self.index > -1:
            result = self.datas[self.index]
            self.index -= 1
            return result

    def min(self):
        if self.index > -1:
            return self.mins[self.index]

    @classmethod
    def test(cls):
        minStack = MinStack()
        minStack.push(1)
        print(minStack.pop())
        minStack.push(2)
        minStack.push(3)
        print(minStack.min())
        minStack.push(1)
        print(minStack.min())