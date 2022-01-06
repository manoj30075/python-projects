"""
A linked deque implementation
author: CS RIT
"""
from typing import Any

from cs_node import LinkedNode


class Deque:
    __slots__ = "__front", "__back", "size"

    def __init__(self) -> None:
        self.__front = None
        self.__back = None
        self.size = 0

    def __str__(self) -> str:  # do not modify
        """ Returns the contents of the deque from front to back"""
        result = "["
        n = self.__front
        while n != None:
            result += " " + str(n.value)
            n = n.link
        result += " ]"
        return result

    def isEmpty(self) -> bool:  # do not modify
        return self.__front == None

    def enqueueBack(self, newValue) -> None:
        """
        Add a new item at the back of the queue
        :param newValue: The new item to add
        :return: None
        """
        newNode = LinkedNode(newValue)
        if self.isEmpty():
            self.__front = newNode
        else:
            self.__back.link = newNode
        self.__back = newNode

    def dequeueFront(self) -> None:
        """
        Removes the item at the front of the deque
        :return: None
        """
        assert not self.isEmpty(), "dequeueFront from empty deque"
        self.__front = self.__front.link
        if self.isEmpty():
            self.__back = None

    def front(self) -> Any:  # do not modify
        """
        Returns the item at the front of the deque
        :return: The item at the front
        """
        assert not self.isEmpty(), "front on empty deque"
        return self.__front.value

    def back(self) -> Any: # do not modify
        """
        Returns the item at the back of the deque
        :return: The item at the back
        """
        assert not self.isEmpty(), "back on empty deque"
        return self.__back.value

    def enqueueFront(self, newValue: Any) -> None:
        """
        Add a new item at the front of the deque
        :param newValue: the new item to add
        :return: None
        """
        # TODO
        new_node = LinkedNode(newValue, self.__front)
        if self.isEmpty():
            self.__back = new_node
        self.__front = new_node


        self.size += 1
    def dequeueBack(self) -> None:
        """
        Remove the item at the back of the deque
        :return: None
        """
        assert not self.isEmpty(), "dequeueBack from empty deque"
        # TODO
        pass


def test() -> None:
    dq = Deque()
    print("Deque's size:", dq.size)
    print(dq)

    for value in 1, 2, 3:
        dq.enqueueFront(value)
    print("Deque's size:", dq.size)
    print(dq)
    print(dq.front())
    print(dq.back())

    # for value in 8, 9, 10:
    #     dq.enqueueBack(value)
    # print("Deque's size:", dq.size)
    # print(dq)
    #
    # print('dequeFront:', dq.front())
    # dq.dequeueFront()
    # print("Deque's size:", dq.size)
    # print(dq)
    #
    # while not dq.isEmpty():
    #     print('dequeBack:', dq.back())
    #     dq.dequeueBack()
    #     print("Deque's size:", dq.size)
    #     print(dq)


if __name__ == "__main__":
    test()
