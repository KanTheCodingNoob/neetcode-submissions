# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        INVALID_NUM = -101
        
        array1 = []
        array2 = []

        def dfs(node, array):
            if node is None:
                array.append(INVALID_NUM)
                return
            array.append(node.val)
            dfs(node.left, array)
            dfs(node.right, array)
        
        dfs(p, array1)
        dfs(q, array2)

        n, m = len(array1), len(array2)
        if n != m:
            return False
        
        for i in range(n):
            if array1[i] != array2[i]:
                return False
        return True