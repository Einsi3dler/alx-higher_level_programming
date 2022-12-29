#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(Node):
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return '\n'.join(str(v) for v in nodes)

    def topIns(self, value):
        new_node = Node(value)
        man = self.head
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            self.head = new_node
            new_node.next = temp
    
    def Ins(self, value):
        temp = self.head
        new = Node(value)

        for node in self:
            if node.data > value:
                temp.next = new
                new.next = node
                return
            temp = node
