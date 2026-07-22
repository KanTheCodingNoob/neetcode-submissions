# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return []

        visited = set()
        queue = deque()

        visited.add(root)
        queue.append(root)

        while queue:
            res.append([])
            for _ in range(len(queue)):
                curr = queue.popleft()
                res[-1].append(curr.val)

                if curr.left and curr.left not in visited:
                    visited.add(curr.left)
                    queue.append(curr.left)
                if curr.right and curr.right not in visited:
                    visited.add(curr.right)
                    queue.append(curr.right)
            

        return res