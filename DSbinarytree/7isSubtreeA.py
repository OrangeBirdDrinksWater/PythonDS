class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def areIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (
        root1.val == root2.val
        and areIdentical(root1.left, root2.left)
        and areIdentical(root1.right, root2.right)
    )


def isSubtree(T, S):
    if S is None:
        return True
    if T is None:
        return False
    if areIdentical(T, S):
        return True
    return isSubtree(T.left, S) or isSubtree(T.right, S)


# Driver program to test above function

""" TREE 1
     Construct the following tree
              26
            /   \
          10     3
        /    \     \
      4      6      3
       \
        30
    """

T = Node(26)
T.right = Node(3)
T.right.right = Node(3)
T.left = Node(10)
T.left.left = Node(4)
T.left.left.right = Node(30)
T.left.right = Node(6)

""" TREE 2
     Construct the following tree
          10
        /    \
      4      6
       \
        30
    """
S = Node(10)
S.right = Node(6)
S.left = Node(4)
S.left.right = Node(30)

if isSubtree(T, S):
    print("Tree 2 is subtree of Tree 1")
else:
    print("Tree 2 is not a subtree of Tree 1")

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
