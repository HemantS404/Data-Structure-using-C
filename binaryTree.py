class node:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def createNode(data, root=None):
    if root == None:
        root = node(data)
        return root
    elif root.data > data:
        root.left = createNode(data,root.left)
    else:
        root.right = createNode(data,root.right)
    return root

def createTree(array):
    rootNode = None
    for data in array:
        rootNode = createNode(data, rootNode)
    return rootNode
        
rootNode = createTree([5,7,6,8,3,4,2,9])

def inorder(root):
    if root == None:
        return
    else:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


def preorder(root):
    if root == None:
        return
    else:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root == None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

preorder(rootNode)
print('')
inorder(rootNode)
print('')
postorder(rootNode)

def iPre(root):
    root = root.left
    if root == None:
        return None
    while(root.right != None):
        root = root.right
    return root.data
def iPost(root):
    root = root.right
    if root == None:
        return None
    while(root.left != None):
        root = root.left
    return root.data

def deleteNode(root,parent,data,loc):
    if root == None:
        return None 
    elif root.data > data:
        deleteNode(root.left,root,data,0)
    elif root.data < data:
        deleteNode(root.right,root,data,1)
    else:
        if root.left==None and root.right==None:
            if loc == 1:
                parent.right = None
            else:
                parent.left = None
        else:
            if iPre(root) != None:
                root.data = iPre(root)
                deleteNode(root.left,root,root.data,0)
            else:
                root.data = iPost(root)
                deleteNode(root.right,root,root.data,1)                

deleteNode(rootNode,None,'value to be deleted',0)

print('')
preorder(rootNode)
print('')
inorder(rootNode)
print('')
postorder(rootNode)