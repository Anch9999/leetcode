from utils.binary_tree_helper import arr_to_binary_tree_helper
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: 'TreeNode') -> 'List[str]':

        def path_helper(cur, res, temp, level):
            if cur:
                while len(temp) > level:
                    temp.pop()
                temp += [cur.val]
                path_helper(cur.left, res, temp, level + 1)
                path_helper(cur.right, res, temp, level + 1)
                if not cur.left and not cur.right:
                    if len(temp) > 1:
                        s = str(temp[0])
                        for i in temp[1:]:
                            s += "->" + str(i)
                        res.append(s)
                    else:
                        res.append(str(temp[0]))

        if not root:
            return []

        res = []
        path_helper(root, res, [], 0)
        return res

if __name__ == '__main__':
    # begin
    s = Solution()
    arr = [1,2,3,None,5]
    print(s.binaryTreePaths(arr_to_binary_tree_helper(arr)))
