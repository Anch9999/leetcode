from utils.binary_tree_helper import arr_to_binary_tree_helper
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':

        def path_helper(cur, path, temp, level):
            if cur:
                while len(temp) > level:
                    temp.pop()
                temp += [cur.val]
                path_helper(cur.left, path, temp, level + 1)
                path_helper(cur.right, path, temp, level + 1)
                if not cur.left and not cur.right:
                    path.append(temp[::-1])

        res = []
        path_helper(root, res, [], 0)
        res.sort()
        ans = ""
        for val in res[0]:
            ans += chr(97 + val)
        return ans

if __name__ == '__main__':
    # begin
    s = Solution()
    arr = [25,1,3,1,3,0,2]
    print(s.smallestFromLeaf(arr_to_binary_tree_helper(arr)))
