class ChainNode:
    __slots__ = 'key', 'value', 'link'

    def __init__(self, key, value, link=None):
        self.key = key
        self.value = value
        self.link = link