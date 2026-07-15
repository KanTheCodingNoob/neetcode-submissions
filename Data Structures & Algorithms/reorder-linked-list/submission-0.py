# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        array = []
        temp = head
        while temp is not None:
            array.append(temp)
            temp = temp.next
        n = len(array)
        l, r = 0, n-1
        while l < r:
            array[l].next = array[r]
            array[r].next = array[l + 1]
            l += 1
            r -= 1
        array[l].next = None
                
        