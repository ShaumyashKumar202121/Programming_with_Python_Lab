# Lab-7: Design a class that accommodates all the Tree traversal types (Inorder, Preorder, Postorder)
#declaring the class node
class Node:
    def __init__(self, data) -> None:
        self.data = data  # datamembers
        self.left = None
        self.right = None

    def linkNode(self, leftNode, rightNode):
        #to link right child to left ones
        self.left = leftNode
        self.right = rightNode
        return

class treeTraversal(object):
    #a class that conatins all type of tree traversaL

    def preorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
        return

    def inorder(self, root):
        #to perform inorder traversal#
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
        return
        
    def postorder(self, root):
        #to perform postorder traversal#
         if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")
         return


# code to check that
# Node 
n1 = Node(3)
n2 = Node(6)
n3 = Node(5)
n4 = Node(4)
n5 = Node(1)
n6 = Node(6)
n7 = Node(7)

# Tree creation
n1.linkNode(n2, n3)
n2.linkNode(n4, n5)
n3.linkNode(n6, n7)

trav = treeTraversal()
trav.preorder(n1)
print()
trav.inorder(n1)
print()
trav.postorder(n1)