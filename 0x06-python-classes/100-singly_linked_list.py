#!/usr/bin/python3
"""
This module is an implementation of single linked lists in python.
this contains two classes, node
"""


class Node:
    """
    This class defines a single node in a linked list
    """

    def __init__(self, data, next_node=None):
        """
        self intializes the data of the instances
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        getter for data val
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        setter for data val
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        getter for next_node val
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter for next_node val
        """
        if (value is None) or (isinstance(value, Node)):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList(Node):
    """
    This class instantiates a singly linked list
    """
    def __init__(self):
        """
        intialization
        """
        self.head = None

    def __iter__(self):
        """
        This is a redefinition of an internal method
        it makees the linked list iterable like a list
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next_node

    def __repr__(self):
        """
        So the class can be printed
        """
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next_node
        return '\n'.join(str(v) for v in nodes)

    def sorted_insert(self, value):
        """
        inserts new nodes and sorts it
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        if self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return

        prev_node = self.head
        for node in self:
            if node.data > value:
                prev_node.next_node = new_node
                new_node.next_node = node
                return
            prev_node = node

        if prev_node.next_node is None:
            prev_node.next_node = new_node
            return
