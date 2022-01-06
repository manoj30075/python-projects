class LinkedNode:
    __slots__ = "value", "link"

    def __init__(self, value, link = None):
        self.value = value
        self.link = link

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "LinkedNode(" + repr(self.value) + "," + repr(self.link) + ")"


class Stack:
    __slots__ = "top", "value"

    def __init__(self):
        self.top = None

    def __str__(self):
        return str(self.top)

    def __repr__(self):
        return "Stack(" + repr(self.top) + ")"

    def is_empty(self):
        return self.top is None

    def push(self, value):
        self.top = LinkedNode(value, self.top)

    def pop(self):
        assert not self.is_empty(), "Stack is empty"
        self.top = self.top.link

    def peek(self):
        assert not self.is_empty(), "Stack is empty"
        return self.top.value

def test_stack():
    s = Stack()
    assert s.is_empty()
    s.push(1)
    assert not s.is_empty()
    s.push(2)
    print(repr(s))
    # print(s.peek())
    s.pop()
    # print(s.peek())
    s.peek()
    s.pop()
    assert s.is_empty()
    # print(s)


if __name__ == "__main__":
    test_stack()


