class Node:
    # constructor
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

# insert the value to make BST
def insert(root,node):
    if root is None:
        root=node
        return root
    # check if value is smaller than root, if smaller then put it to left
    if node.value<root.value:
        root.left=insert(root.left,node)

    if node.value>root.value:
        root.right=insert(root.right,node)

    return root

# print root first then left then right
def preorder(root):
    if root:
        print (root.value)
        preorder(root.left)
        preorder(root.right)
# print left, root then right
def inorder(root):
    if root:
        inorder(root.left)
        print (root.value)
        inorder(root.right)

# first left then right then root is printed
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)
#find the minimum value in the tree which is always the leftmost value
def getMinValue(root):
    if root:
        while root.left is not None:
            root=root.left
        return root

def deleteNode(root,value):
    if root is None:
        return root
    # find the "value" in the tree
    if value<root.value:
        root.left=deleteNode(root.left,value)
    elif value>root.value:
        root.right=deleteNode(root.right,value)
    # perform delete after the value is found
    else:
        # three possiblity of node
        # check if left node is null, if left is null the return right node
        if root.left is None:
            temp=root.right
            root=None
            return temp
        # check if right node is null, if right is null the return left node
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        # when tree has node child both side
        else:
            # get the smallest value of the right sub tree
            temp=getMinValue(root.right).value
            root.value   =temp
            # the left most is still in the tree which needs to be deleted
            root.right=deleteNode(root.right,temp)
    return root





root=Node(50)
insert(root,Node(10))
insert(root,Node(2))
insert(root,Node(80))
insert(root,Node(15))
insert(root,Node(60))
insert(root,Node(90))

# preorder(root)
# inorder(root)
# postorder(root)
# print(getMinValue(root).value)
deleteNode(root,50)
postorder(root)