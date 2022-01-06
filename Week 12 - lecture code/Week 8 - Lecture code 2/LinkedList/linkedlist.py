"""
linkedlist.py

A Linked List interface and implementation in Python
This version uses a cursor. Using indices is inherently inefficient and
hides the strengths of the linked list.
Cursors, immutable, are created by list methods.

auteur: James Heliotis
"""
from typing import Any

from node import LinkedNode

class LinkedList:

    __slots__ = 'front'
    front: LinkedNode

    def __init__( self ) -> None:
        """ Create an empty list.
        """
        self.front = None

    def append( self, new_value: Any ) -> None:
        """ Add value to the end of the list.
            List is modified.
            :param new_value: the value to add
            :return: None
        """
        node = self.front
        newNode = LinkedNode( new_value )
        if node == None:
            self.front = newNode
        else:
            while node.link != None:
                node = node.link
            node.link = newNode

    def prepend( self, new_value: Any ) -> None:
        """ Add value to the beginning of the list.
            List is modified.
            :param new_value: the value to add
            :return: None
        """
        self.front = LinkedNode( new_value, self.front )

    def start( self ) -> LinkedNode:
        """ Generate a cursor that refers to the beginning of the list.
            List is unchanged.
            :return: a cursor, possibly 'off' if list is empty
        """
        return self.front

    def is_off( self, cursor: LinkedNode ) -> bool:
        """ Is the cursor off the list?
            :param cursor: the cursor (list position) to be tested
            :return: True iff the cursor is not at a valid location in the list.
        """
        return cursor == None

    def get_value( self, cursor: LinkedNode ) -> Any:
        """ Get the value at the location indicated by the cursor.
            List is unchanged.
            :pre: not self.is_off( cursor );
                            raises ValueError in event of violation
            :param cursor: the list position of the desired value
            :return: value stored at cursor's location
        """
        if self.is_off( cursor ):
            raise ValueError()
        return cursor.value

    def set_value( self, cursor: LinkedNode, new_value: Any ) -> None:
        """ Change the value at the location indicated by the cursor.
            List is modified.
            :pre: not self.is_off( cursor )
            :param cursor: the list position of the value to be changed
            :return: None
        """
        if self.is_off( cursor ):
            raise ValueError()
        cursor.value = new_value

    def next_loc( self, cursor: LinkedNode ) -> LinkedNode:
        """ Create a new cursor to the next position in the list, or
            'off' if cursor is at the last position.
            List is unmodified.
            :pre: not self.is_off( cursor )
                            raises ValueError in event of violation
            :param cursor: the list position
            :return: the new cursor
        """
        if self.is_off( cursor ):
            raise ValueError()
        return cursor.link

    def insert( self, cursor: LinkedNode, new_value: Any ) -> None:
        """ Place a new value in the list, just before the position
            of the cursor. If the cursor is 'off', this method works
            just like the append method.
            List is modified.
            The cursor still refers the location it did in the list
                before this method was called.
            :param cursor: the list position
            :param new_value: the value to be placed before the cursor position
            :return: None
        """
        if cursor == self.front:
            self.prepend( new_value )
        else:
            node = self.front
            while node.link != cursor:
                node = node.link
            node.link = LinkedNode( new_value, cursor )

    def size( self ) -> int:
        """ Return the number of data elements in this list.
            :post: result >= 0
        """
        return self._size_to_end( self.front )

    def _size_to_end( self, node: LinkedNode ) -> int:
        if node == None:
            return 0
        else:
            return 1 + self._size_to_end( node.link )

def print_list( seq: LinkedList, msg: str ) -> None:
    """ Print the contents of a list on a single line, first to last.
    """
    print( "%s\n===============\n[%d] " % ( msg, seq.size() ), end="" )
    cursor = seq.start()
    while not seq.is_off( cursor ):
        print( seq.get_value( cursor ), end=" " )
        cursor = seq.next_loc( cursor )
    print()

def test() -> None:
    # Create a list.
    seq = LinkedList()
    print_list( seq, "START" )

    # Add values using append.
    for even in 4, 6:
        seq.append( even )

    # Prepend a value
    seq.prepend( 2 )
    print_list( seq, "EVENS" )

    # Weave additional elements in to the list.
    odd = 1
    cursor = seq.start()
    while not seq.is_off( cursor ):
        seq.insert( cursor, odd )
        odd += 2
        cursor = seq.next_loc( cursor )
    seq.insert( cursor, odd )

    print_list( seq, "UPTO7" )

    # Test the set_value method.
    seq.set_value( seq.start(), -1 )
    print_list( seq, "NEGTV" )

if __name__ == "__main__":
    test()

