# A Python class that represents an individual node
# in a Binary Tree


from collections import deque


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# create a root
# root = Node(1)
"""
Following is the tree afte above statement
             1
           /    \
        None    None
"""
# root.left = Node(2)
# root.right = Node(3)
"""
2 and 3 becomes left and right children of 1
                    1
                /       \
             2              3
           /    \        /      \
        None    None   None     None
"""

# root.left.left = Node(4)
"""
4 becomes left child of 2
                1
            2       3
        4   None    None    None
    None    None
"""

#Traversal Mechanism  -- Recursive Version

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# Non Recursive Version


def inorder_iter(root):
    if root is not None:
        stck = []  # declare a stack
        curnode = root
        while stck or curnode:
            if curnode is not None:
                stck.append(curnode)
                curnode = curnode.left
            else:
                curnode = stck.pop()
                print(curnode.data, end=" ")
                curnode = curnode.right


def preorder_iter(root):
    if root:
        stck = []  # declare a stack
        stck.append(root)
        curnode = None
        while stck:
            curnode = stck.pop()
            # process current node
            print(curnode.data, end=" ")
            if curnode.right is not None:
                stck.append(curnode.right)
            if curnode.left is not None:
                stck.append(curnode.left)

def postorder_iter(root):
    if root is not None:
        stck = []  # declare a stack
        curnode = root
        while stck or curnode:
            if curnode is not None:
                stck.append(curnode)
                curnode = curnode.left
            else:
                curnode = stck.pop()
                print(curnode.data, end=" ")
                curnode = curnode.right


# Level Order Traversal Implementation


def levelorder(root):
    if root:
        q = deque()  # declare an empty queue
        q.append(root)
        while q:
            temp = q.popleft()
            print(temp.data, end=" ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)


# Driver code
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    root.left.left.left = Node(5)
    root.left.left.right = Node(4)
    print("Inorder Traversal -->")
    inorder(root)
    print("\nInorder Traversal Iterative-->")
    inorder_iter(root)
    print("\nPreorder Traversal -->")
    preorder(root)
    print("\nPreorder Traversal Iterative-->")
    preorder_iter(root)
    print("\nPostorder Traversal -->")
    postorder(root)
    print("\nLevel Order Traversal -->")
    levelorder(root)
