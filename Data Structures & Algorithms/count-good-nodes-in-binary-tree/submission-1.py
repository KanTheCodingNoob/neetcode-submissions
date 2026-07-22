# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, currMax):
            if currMax <= node.val:
                currMax = node.val
                self.count += 1
            if node.left:
                dfs(node.left, currMax)
            if node.right:
                dfs(node.right, currMax)
        
        dfs(root, -101)
        return self.count