# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        
        overflow = 0

        newHead = ListNode()
        curr = newHead

        while p1 and p2:
            result = curr.val + p1.val + p2.val
            curr.val = result % 10
            overflow = result // 10
            curr.next = ListNode(overflow)
            curr = curr.next
            p1 = p1.next
            p2 = p2.next
        
        while p1:
            result = curr.val + p1.val
            curr.val = result % 10
            overflow = result // 10
            curr.next = ListNode(overflow)
            curr = curr.next
            p1 = p1.next
        
        while p2:
            result = curr.val + p2.val
            curr.val = result % 10
            overflow = result // 10
            curr.next = ListNode(overflow)
            curr = curr.next
            p2 = p2.next
        
        clean = newHead
        while clean.next != curr:
            clean = clean.next
        clean.next = None if (clean.next.val == 0) else curr

        return newHead
