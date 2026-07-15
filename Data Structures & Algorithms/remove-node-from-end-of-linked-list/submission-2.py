# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        if size == 1:
            return None
        idx = size - n
        newHead = ListNode(0, head)
        temp = newHead
        while idx != 0:
            temp = temp.next
            idx -= 1
        temp.next = temp.next.next
        return newHead.next
        