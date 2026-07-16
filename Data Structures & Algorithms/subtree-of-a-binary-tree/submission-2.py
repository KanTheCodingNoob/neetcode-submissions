# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        array1 = [] # OG
        array2 = [] # Child?

        def dfs(node, array):
            if node is None:
                array.append(-101)
                return
            array.append(node.val)
            dfs(node.left, array)
            dfs(node.right, array)
        
        dfs(root, array1)
        dfs(subRoot, array2)

        m, n = len(array1), len(array2)
        for i in range(m):
            if array1[i] == array2[0]:
                found = True
                for j in range(n):
                    if array1[i + j] != array2[j]:
                        found = False
                        break
                if found:
                    return True
            
        
        return False