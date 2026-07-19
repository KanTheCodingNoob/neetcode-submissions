"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        hashmap = {} # OG to new
        visited = set()

        def dfs(n):
            if n not in hashmap:
                hashmap[n] = Node(n.val, [])
            visited.add(n)
            for m in n.neighbors:
                if m not in visited:
                    dfs(m)

        dfs(node)

        for key, val in hashmap.items():
            for n in key.neighbors:
                val.neighbors.append(hashmap[n])

        return hashmap[node]