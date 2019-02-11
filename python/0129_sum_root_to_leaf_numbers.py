from utils.binary_tree_helper import arr_to_binary_tree_helper
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNodes(self, cur, val):
        if cur:
            self.sumNodes(cur.left, val * 10 + cur.val)
            self.sumNodes(cur.right, val * 10 + cur.val)
            if not cur.left and not cur.right:
                self.ans += val * 10 + cur.val


    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        if not root:
            return 0

        self.sumNodes(root, 0)
        return self.ans

if __name__ == '__main__':
    # begin
    s = Solution()
    arr = [4,9,0,5,1]
    print(s.sumNumbers(arr_to_binary_tree_helper(arr)))
