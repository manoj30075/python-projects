from chainnode import ChainNode


class ChainList:
    __slots__ = "head", "add", "size"

    def __init__(self, head=None):
        """
        Initialises the ChainList with Key and value pair
        :param key:
        :param value:
        """
        self.head = head
        self.size = 0

    def __iter__(self):
        """
        overridden iterator for ChainList
        :return:
        """
        temp_head = self.head
        while temp_head is not None:
            yield temp_head
            temp_head = temp_head.link

    def __str__(self):
        string = ""
        temp = self.head
        while temp is not None:
            string += temp.key + " " + str(temp.value) + "\n"
            temp = temp.link
        return string

    def prepend(self, key, value):
        """
        Prepends the ChainNode to the chain list
        :param key:
        :param value:
        :return:
        """
        self.size += 1
        new_node = ChainNode(key, value)
        new_node.link = self.head
        self.head = new_node

    def contains(self, key):
        """
        Checks if the key is present in the chain list
        :param key:
        :return:
        """
        head = self.head

        while head is not None:
            if head.key == key:
                return True
            head = head.link
        return False

    def get(self, key):
        """
        Returns the value when key is given
        :param key:
        :return:
        """
        head = self.head
        while head is not None:
            if head.key == key:
                return head.value
            head = head.link
        return None

    def remove(self, key):
        """
        Remove chained node when key is passed
        :param key:
        :return:
        """
        head = self.head

        if head is None:
            return False

        if head.link is None:
            if head.key == key:
                self.size -= 1
                self.head = None
                return True
            return False

        while head.key is not key:
            if head.link is None and head.key != key:
                return False
            head = head.link

        if head.link is None:
            return False
        head.link = head.link.link
        self.size -= 1
        return True

    def put(self, key, value):
        """
        Updates the value based on the key
        :param key:
        :param value:
        :return:
        """
        head = self.head

        while head is not None:
            if head.key == key:
                head.value = value
            head = head.link