# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.found = False
        self.LCA = None
        
        def dfs(node) -> bool:
            if node is None:
                return False
            l = dfs(node.left)
            r = dfs(node.right)
            n = False
            if node.val == p.val or node.val == q.val:
                n = True
            if (l == r == True or l == n == True or r == n == True) and self.found is False:
                self.LCA = node
                self.found = False
            if l == True or r == True:
                return True
            return n
        
        dfs(root)
        return self.LCA
            