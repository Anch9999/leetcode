class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class DoubleLinkNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
