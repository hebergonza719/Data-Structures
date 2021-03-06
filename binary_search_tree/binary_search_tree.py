"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class Stack:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)
    
    def pop(self):
        if len(self.array) > 0:
            return self.array.pop()


class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, value):
        self.array.insert(0, value)

    def dequeue(self):
        if len(self.array) > 0:
            return self.array.pop()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is target:
            return True
        elif self.value > target and self.left:
            if self.left.value is target:
                return True
            else:
                return self.left.contains(target)
        elif self.value < target and self.right:
            if self.right.value is target:
                return True
            else:
                return self.right.contains(target)
        return False


    # Return the maximum value found in the tree
    def get_max(self):
        cur_node = self
        max_value = self.value
        if cur_node.right is None:
            return max_value
        while cur_node:
            max_value = cur_node.value
            cur_node = cur_node.right
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        queue = Queue()
        queue.enqueue(self)

        while len(queue.array) > 0:
            cur_node = queue.dequeue()
            print(cur_node.value)
            if cur_node.left:
                queue.enqueue(cur_node.left)
            if cur_node.right:
                queue.enqueue(cur_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = Stack()
        stack.push(self)

        while len(stack.array) > 0:
            cur_node = stack.array.pop()
            print(cur_node.value)
            if cur_node.right:
                stack.push(cur_node.right)
            if cur_node.left:
                stack.push(cur_node.left)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()
bst.in_order_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
