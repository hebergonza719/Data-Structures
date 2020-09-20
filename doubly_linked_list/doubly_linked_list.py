"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev = prev_node
        self.next = next_node

    # updates next and previous pointer for those next to the node
    def delete(self):
        # if there is a previous pointer - not for head
        if self.prev:
            self.next.prev = self.prev
        # if there is a next pointer - not for tail
        if self.next:
            self.prev.next = self.next

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create new_node
        new_node = ListNode(value)
        # 1. add to empty DLL
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 2. add to nonempty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # update length
        self.length += 1


    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        self.length -= 1
        if self.head is None:
            return None
        else:
            # if it has one item
            head_node = self.head
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                #if it has 2 or more elements
                self.head = head_node.next
                self.head.prev = None
            return head_node.value


    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        self.length -= 1
        if self.head is None:
            return None
        else:
            tail_node = self.tail
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = tail_node.prev
                self.tail.next = None
        return tail_node.value                

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return None
        self.delete(node)
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return None
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # don't need to return value

        # Do need to update head, tail
        # list is empty
        if self.head is None:
            return None
        # list has one element
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        # list has 2 or more elements
        elif node is self.head:
            self.head = node.next
            self.head.prev = None
            # node.delete()
        elif node is self.tail:
            self.tail = node.prev
            self.tail.next = None
            # node.delete()
        else:
            # remove from middle
            node.delete()

        self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return None
        else:
            cur_node = self.head
            max_value = self.head.value
            while cur_node is not None:
                if max_value < cur_node.value:
                    max_value = cur_node.value
                cur_node = cur_node.next
            return max_value


# example = DoublyLinkedList()
# example.add_to_head(100)
# example.add_to_head(101)
# example.add_to_head(102)
# example.add_to_head(103)
# print("second", example.head.next.value)
# example.delete(example.head.next)
# print("old head", example.head.value)
# print("new second", example.head.next.value)
# example.delete(example.head.next)
# print("new new second", example.head.next.value)
# example.delete(example.tail)
# print("new tail should be 103 == ", example.tail.value)
# print(example.head.value == example.tail.value)