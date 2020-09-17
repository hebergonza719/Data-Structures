class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        # if LL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(new_node)
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        # if LL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None
        else:
            ret_value = self.head.get_value()
            # if LL has one element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # if LL has two or more elements
            else:
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):
        # empty list?

        # list with 1 element?

        # list with +2 elements?
        pass
