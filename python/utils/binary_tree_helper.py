from collections import deque


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


# Use python collections.deque because lists are not efficient to do this
def insert_node(temp, val):
    q = deque([])
    q.append(temp)
    while q:
        temp = q.popleft()
        if not temp.val:
            continue

        if not temp.left:
            temp.left = Node(val)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(val)
            break
        else:
            q.append(temp.right)


def arr_to_binary_tree_helper(arr):
    """
    :tpye arr: List
    :rtype: Node
    """
    if len(arr) == 0:
        return Node()
    else:
        for i in range(len(arr)):
            if i == 0:
                root = Node(arr[i])
            else:
                insert_node(root, arr[i])
        return root
