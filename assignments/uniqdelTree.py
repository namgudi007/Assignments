def insert(root, node):
    # temp = node(elem)

    if root is None:
        root = node

    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def display(root, i):

    if(root is not None):
        display(root.right, i+1)
        j = 1
        while(j <= i):
            print(end="     ")
            j = j+1
        print(root.val)
        display(root.left, i+1)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inodr.append(root.val)
        inorder(root.right)


def delete(root, elem):
    if root is None:
        print("element not found")
        return root
    if (root.right is None and root.left is None):
        return None
    if elem < root.val:
        root.left = delete(root.left, elem)
    elif(elem > root.val):
        root.right = delete(root.right, elem)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        current = root.right
        while(current.left is not None):
            current = current.left
        temp = current
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    return root


class node:
    def __init__(self, elem):
        self.left = None
        self.right = None
        self.val = elem


n = int(input("n = "))
elem = list(map(int, input().rstrip().split()))
inodr = []
root = node(elem[0])
for i in range(1, n):
    insert(root, node(elem[i]))

print("the following is the tree format")
display(root, 0)
print("the inorder traversal is")
inorder(root)
print("\n")

while True:
    d = int(input("Enter the element to be deleted"))
    delete(root, d)
    print("The tree again")
    display(root, 0)
    print("the inorder traversal is")
    inorder(root)
