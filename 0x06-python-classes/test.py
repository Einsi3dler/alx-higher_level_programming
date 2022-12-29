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
    
    def Ins(self, target_node_data, new_node):
        prev_node = self.head
        for node in self:
            if node.data > target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
