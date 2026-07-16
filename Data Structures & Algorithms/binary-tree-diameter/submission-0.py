# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDmt = 0
        
        def dfs(curr):
            if curr is None:
                return 0
            l = dfs(curr.left)
            r = dfs(curr.right)
            self.maxDmt = max(l + r, self.maxDmt)
            return 1 + max(l, r)

        h = dfs(root)

        return self.maxDmt
    
        