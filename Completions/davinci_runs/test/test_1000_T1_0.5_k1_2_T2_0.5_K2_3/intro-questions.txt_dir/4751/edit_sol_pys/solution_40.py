# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        slow = head.next
        fast = head.next.next

        while fast is not None and fast.next is not None:
            if fast == slow:
                return True

            slow = slow.next
            fast = fast.next.next

        return False
