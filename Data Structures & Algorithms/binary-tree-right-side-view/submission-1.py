# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque()
        res = []

        q.append(root)
        res.append(root.val)

        level = 1

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr.right:
                    q.append(curr.right)
                    if len(res) == level:
                        res.append(curr.right.val)
                if curr.left:
                    q.append(curr.left)
                    if len(res) == level:
                        res.append(curr.left.val)
            level += 1
        
        return res
            