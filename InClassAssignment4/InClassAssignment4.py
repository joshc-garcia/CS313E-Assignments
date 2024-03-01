# Inclass Assignment
from example_009_binary_search_tree import Node
from example_009_binary_search_tree import BST 
import math

class Node():
    def __init__(self, key):
        self.key = key
        self.lChild = None
        self.rChild = None

    def bst_size(self, node):
        size = 0

        if node != None:
            size += 1
            if node.rChild != None:
                node.bst_size(node.lChild)
                size += 1
            if node.lChild != None:
                node.bst_size(node.rChild)
                size += 1
        
        return size
    
class BST():
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def insert(self, val):
        newNode = Node(val)

        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
# seearch 
            while (current != None):
                parent = current
                if (val < current.key):
                    current = current.lChild
                else:
                    current = current.rChild
# insert 
            if (val < parent.key):
                parent.lChild = newNode
            else:
                parent.rChild = newNode

    # use in order traversal for this
    def sort(self):
        sort_list = []
        self.in_order_traversal(self.root, sort_list)
        return sort_list

    def in_order_traversal(self, node, sort_list):
        if node:
            self.in_order_traversal(node.lChild, sort_list)
            sort_list.append(node.key)
            self.in_order_traversal(node.rChild, sort_list)

    def bst_median(self):
        sorted_elements = self.sort()

        if (len(sorted_elements) % 2 != 0):
            return (sorted_elements[len(sorted_elements) // 2])
        else:
            right_element = sorted_elements[(len(sorted_elements) // 2)]
            left_element = sorted_elements[((len(sorted_elements) // 2) - 1)]
            return (right_element + left_element) / 2
        
    def height(self):
        return self.calculate_height(self.root)
            
    def calculate_height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.calculate_height(node.lChild)
            right_height = self.calculate_height(node.rChild)
            return max(left_height, right_height) + 1

    def is_balanced(self):
        left_height = self.calculate_height(self.root.lChild)
        right_height = self.calculate_height(self.root.rChild)

        if (abs(left_height - right_height) <= 1):
            return True
        else:
            return False

def main():
    # node_root = Node(1)
    # print(node_root.bst_size(node_root))
    bst = BST()
    bst.insert(10)
    bst.insert(40)
    bst.insert(5)
    bst.insert(15)
    bst.insert(22)
    bst.insert(4)
    print(bst.sort())
    print(bst.bst_median())
    print(bst.height())
    print(bst.is_balanced())


if __name__ == '__main__':
    main()