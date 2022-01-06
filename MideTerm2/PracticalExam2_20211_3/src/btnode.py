"""
CSCI-603: Trees (week 10)
Author: RIT CS

This is an implementation of a binary tree node.
"""
from typing import Any


class BTNode:
    """
    A binary tree node contains:
     :slot value: A user defined value
     :slot left: A left child (BTNode or None)
     :slot right: A right child (BTNode or None)
    """
    __slots__ = 'value', 'left', 'right'
    val: Any
    left: 'BTNode'
    right: 'BTNode'

    def __init__(self, value: Any, left: 'BTNode' = None, right: 'BTNode' = None) -> None:
        """
        Initialize a node.
        :param value: The value to store in the node
        :param left: The left child (BTNode or None)
        :param right: The right child (BTNode or None)
        :return: None
        """
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "BTNode(" + str(self.left) + "," + str(self.value) + \
               "," + str(self.right) + ")"


def buildTestTree():
    """
    Build a tree
    :return: The tree depicted in Figure 1 on the exam.
    """
    left = BTNode(4,
                  BTNode(2,
                         None,
                         None),
                  BTNode(5,
                         None,
                         None))
    right = BTNode(12,
                   BTNode(9,
                          None,
                          BTNode(10, None, None)),
                   BTNode(15,
                          None,
                          None))
    return BTNode(7, left, right)


def printDescendingOrder(root: BTNode) -> None:
    """
    Prints in a single line the tree's content in descending order
    :param root: The tree's root
    :return: None
    """
    # TODO
    pass


def pathToAncestor(node: BTNode, desValue: Any, ancValue: Any):
    """
    Compute the ancestor's path between the node with value
    desValue and the node with value ancValue
    :pre: The tree is a binary search tree
    :param node: the assumed root of the tree
    :param desValue: the descendant node's value
    :param ancValue: the ancestor node's value
    :return: The list of all nodes between the node with
    the value desValue and the node with the value ancValue
    in order from deepest to shallowest
    """
    if(node is ancValue):

    pass


def testBTNode() -> None:
    """
    A test function for BTNode.
    :return: None
    """
    left = BTNode(10)
    right = BTNode(30)
    parent = BTNode(20)
    parent.left = left
    parent.right = right
    print('parent (20):', parent.value)
    print('left (10):', parent.left.value)
    print('right (30):', parent.right.value)

    # testing build tree
    tree = buildTestTree()
    print("Testing buildTree function..........")
    print(tree)
    print()

    # testing print descending order
    print("Testing printDescendingOrder function..........")
    printDescendingOrder(parent)
    print()
    printDescendingOrder(tree)
    print()

    # testing path
    print("Testing path function..........")
    print("Path from", 10, "to", 7, "is", pathToAncestor(tree, 10, 7))
    print("Path from", 10, "to", 12, "is", pathToAncestor(tree, 10, 12))
    print("Path from", 2, "to", 7, "is", pathToAncestor(tree, 2, 7))
    print("Path from", 4, "to", 4, "is", pathToAncestor(tree, 4, 4))
    print()


if __name__ == '__main__':
    testBTNode()
