"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

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
            self.head == new_node
            self.tail == new_node
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
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
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
        pass

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
            # self.head.prev = None
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            # self.tail.next = None
            node.delete()
        else:
            # remove from middle
            node.delete()

        self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass


example = DoublyLinkedList()
print(example.length)
example.add_to_head(1)
print(example.length)