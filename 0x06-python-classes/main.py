#!/usr/bin/python3
LinkedList = __import__('test').LinkedList
Node = __import__('test').Node

llist = LinkedList()
llist.topIns(6)
llist.topIns(5)
llist.topIns(4)
llist.topIns(3)
llist.topIns(2)
llist.topIns(1)
print(llist)
new = Node(4)  
llist.Ins(4, new)
print(llist)
