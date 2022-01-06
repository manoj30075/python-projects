"""
file: hashmap.py
description: HashMap created on Chained hash tables
language: python3
author: Manoj Kumar Reddy Palasamudram , mp6112@rit.edu
        Ashwath Sreedhar Halemane, ah7387@rit.edu
"""
from typing import Any, Callable, Hashable

from chainnode import ChainNode
from chainlist import ChainList

class HashMap:
    __slots__ = 'hash_func', 'initial_num_buckets', 'load_limit', 'table', "size"
    MIN_BUCKETS = 10

    def __init__(
            self,
            hash_func: Callable[[Hashable], int] = hash,
            initial_num_buckets: int = 100,
            load_limit: float = 0.75
    ) -> None:
        """Create a new hash table."""
        self.hash_func = hash_func
        if initial_num_buckets < self.MIN_BUCKETS:
            self.initial_num_buckets = self.MIN_BUCKETS
        else:
            self.initial_num_buckets = initial_num_buckets
        self.load_limit = load_limit
        self.table = [None] * initial_num_buckets
        self.size = 0

    def __iter__(self):
        """Return an iterator of all values in this hash table."""
        for i in self.table:
            if i is not None:
                for j in i:
                    yield j.key, j.value

    def __str__(self):
        """Return a string representation of this hash table."""
        string = ""
        for i in self.table:
            if i is not None:
                string += "Chain list: " + str(i)

        return string

    def add_to_new_table(self, key, value, table):
        hash_value = self.hash_func(key)
        bucket_index = hash_value % self.initial_num_buckets
        new_node = ChainNode(key, value)
        if table[bucket_index] is None:
            table[bucket_index] = ChainList(new_node)
            self.size += 1
        else:
            if table[bucket_index].contains(key):
                table[bucket_index].put(key, value)
            else:
                chain_node = table[bucket_index]
                chain_node.prepend(key, value)
                self.size += 1

    def rehash(self):
        """Resize the hash table to have a number of buckets equal to the size."""
        new_table = [None] * self.initial_num_buckets
        temp_table = self.table
        self.table = new_table
        for i in temp_table:
            if i is not None:
                for node in i:
                    self.add(node.key, node.value)

    def get_bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        hash_value = self.hash_func(key)
        return hash_value % self.initial_num_buckets

    def add(self, key: Hashable, value: Any) -> None:
        """Add a key-value pair to the hash table."""
        bucket_index = self.get_bucket_index(key)
        if self.size / self.initial_num_buckets > self.load_limit:
            self.initial_num_buckets *= 2
            self.rehash()

        new_node = ChainNode(key, value)
        if self.table[bucket_index] is None:
            self.size += 1
            self.table[bucket_index] = ChainList(new_node)
        else:
            if self.table[bucket_index].contains(key):
                self.table[bucket_index].put(key, value)
            else:
                chain_node = self.table[bucket_index]
                chain_node.prepend(key, value)
                self.size += 1

    def contains(self, key: Hashable):
        """Return True if the hash table contains the given key, or False otherwise."""
        bucket_index = self.get_bucket_index(key)
        node = self.table[bucket_index]

        if node is None:
            return False
        else:
            return node.contains(key)

    def get(self, key):
        """Return the value associated with the given key"""
        bucket_index = self.get_bucket_index(key)
        node = self.table[bucket_index]

        if node is None:
            return None
        return node.get(key)

    def remove(self, key):
        """Remove the given key from this hash table"""
        bucket_index = self.get_bucket_index(key)
        node = self.table[bucket_index]

        if node is None:
            return False
        if node.remove(key):
            self.size -= 1
            if self.size / self.initial_num_buckets < 1 - self.load_limit:
                if int(self.initial_num_buckets/2) < self.MIN_BUCKETS:
                    self.initial_num_buckets = 10
                else:
                    self.initial_num_buckets //= 2
                self.rehash()
            return True
        return False

    def imbalance(self):
        """Return the ratio of the number of items to the number of buckets."""
        length = 0
        for i in self.table:
            if i is not None:
                length += 1

        return self.size / length - 1



