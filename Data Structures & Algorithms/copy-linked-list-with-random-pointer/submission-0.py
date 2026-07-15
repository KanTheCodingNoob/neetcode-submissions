"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        
        newHead = Node(0)
        curr = newHead

        temp = head

        # Create a new list while storing a hashmap of original and new node
        while temp:
            curr.next = Node(temp.val)

            hashmap[temp] = curr.next

            temp = temp.next
            curr = curr.next
        
        # Link it with
        temp = head
        while temp:
            if temp.random is not None:
                hashmap[temp].random = hashmap[temp.random]
            temp = temp.next
        
        return newHead.next
