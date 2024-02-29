# Inclass Assignment
from example_009_binary_search_tree import Node
from example_009_binary_search_tree import BST 

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

        if self.root != None:
            if self.root.rChild != None:
                self.sort(self.root.lChild)
                sort_list.append(self.root.lChild)
            if self.root.lChild != None:
                self.sort(self.root.rChild)
                sort_list.append(self.root.rChild)

        return sort_list
            #     self.root.rChild.sort()
            #     sort_list.append(self.root.rChild)
            # if self.root.lChild != None:
            #     self.root.lChild.sort()
            #     sort_list.append(self.root.lChild)

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
    bst.sort()

if __name__ == '__main__':
    main()