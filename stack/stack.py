"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.array = []
#
#     def __len__(self):
#         return self.size
#
#     def push(self, value):
#         self.array.append(value)
#         self.size = self.size + 1
#
#     def pop(self):
#         ret_val = None
#
#         if self.size > 0:
#             ret_val = self.array[self.size - 1]
#
#             self.array.pop()
#             self.size = self.size - 1
#
#         return ret_val


import sys
sys.path.insert(1, '../singly_linked_list/')


from singly_linked_list import LinkedList, Node


class Stack:
    def __init__(self):
        self.size = 0
        self.linkedList = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        new_node = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = new_node
        elif self.linkedList.head is not None and self.linkedList.tail is None:
            self.linkedList.head.set_next_node(new_node)
            self.linkedList.tail = new_node
        else:
            self.linkedList.add_to_tail(value)
        self.size = self.size + 1

    def pop(self):
        if self.linkedList.head is None:
            self.size = 0
            return None
        else:
            ret_value = None
            if self.linkedList.head is not None and self.linkedList.tail is None:
                ret_value = self.linkedList.head.get_value()
                self.linkedList.head = None
            elif self.size == 2:
                ret_value = self.linkedList.tail.get_value()
                self.linkedList.tail = None
                self.linkedList.head.set_next_node(None)
            elif self.size > 2:
                ret_value = self.linkedList.tail.get_value()
                self.linkedList.tail = self.linkedList.tail.get_prev_node()
            self.size = self.size - 1
            return ret_value


# the difference between using an array and a linked list is that the array stores all the
# elements together side-by-side and the linked list doesn't.
# the list has built in methods that facilitate these operations. 
