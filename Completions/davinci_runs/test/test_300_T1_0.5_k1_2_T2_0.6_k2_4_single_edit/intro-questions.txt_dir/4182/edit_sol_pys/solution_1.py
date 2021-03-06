# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        
        if head.val == val:
            return self.removeElements(head.next, val)
        
        head.next = self.removeElements(head.next, val)
        
        return head
