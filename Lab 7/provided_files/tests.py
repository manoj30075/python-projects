"""
file: tests.py
description: Verify the chained hash map class implementation
"""

__author__ = ["Manoj kumar reddy Palasamudram", "Ashwath Halemane"]

from hashmap import HashMap


def print_map(a_map):
    for word, counter in a_map:  # uses the iter method
        print(word, counter, end=" ")
    print()


def test0():
    table = HashMap(initial_num_buckets=10)
    table.add("to", 1)
    table.add("do", 1)
    table.add("is", 1)
    table.add("to", 2)
    table.add("be", 1)

    print_map(table)

    print("'to' in table?", table.contains("to"))
    print("'to' appears", table.get("to"), "times")
    table.remove("to")
    print("'to' in table?", table.contains("to"))

    print_map(table)


def test1():
    table = HashMap(initial_num_buckets=10)
    table.add("a", 1)
    table.add("b", 1)
    table.add("c", 1)
    table.add("d", 2)
    table.add("e", 1)
    table.add("f", 1)
    table.add("g", 1)
    print("before resizing hash table, table size: " + str(table.initial_num_buckets))
    print("table imbalance: " + str(table.imbalance()))
    table.add("h", 1)
    table.add("i", 2)
    table.add("j", 1)
    table.add("k", 1)
    table.add("m", 1)
    print("after resizing hash table, table size: " + str(table.initial_num_buckets))
    print("table imbalance: " + str(table.imbalance()))


def test2():
    table = HashMap(initial_num_buckets=10)
    table.add("a", 1)
    table.add("b", 1)
    table.add("c", 1)
    table.add("d", 2)
    table.add("e", 1)
    table.add("f", 1)
    table.add("g", 1)
    print("before resizing hash table, table size: " + str(table.initial_num_buckets))
    print("table imbalance: " + str(table.imbalance()))
    table.add("h", 1)
    table.add("i", 2)
    table.add("j", 1)
    table.add("k", 1)
    table.add("m", 1)
    print("after resizing hash table, table size: " + str(table.initial_num_buckets))
    print("table imbalance: " + str(table.imbalance()))
    table.remove("a")
    table.remove("b")
    table.remove("c")
    table.remove("d")
    table.remove("e")
    table.remove("f")
    print("after resizing hash table, table size: " + str(table.initial_num_buckets))
    print("table imbalance: " + str(table.imbalance()))


def test3():
    table = HashMap(initial_num_buckets=5)
    print("Hash map bucket length ", table.initial_num_buckets)


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
