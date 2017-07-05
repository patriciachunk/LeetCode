# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(L, R):
            if not L and not R:
                return True
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root, root)

if __name__ == '__main__':
    result = Solution().isSymmetric([1, 2, 2, 3, 4, 4, 3])
    print result
