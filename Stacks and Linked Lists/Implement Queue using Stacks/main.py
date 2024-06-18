class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.stack2:
            return self.stack2.pop()
        elif self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return None
    def peek(self):
        """
        :rtype: int
        """

        if self.stack2:
            x = self.stack2.pop()
            self.stack2.append(x)
            return x
        elif self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            x = self.stack2.pop()
            self.stack2.append(x)
            return x
        return None

    def empty(self):
        """
        :rtype: bool
        """
        return not (self.stack1 or self.stack2)


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(2)
print(obj.values)
print(obj.pop())
print(obj.peek())
print(obj.empty())