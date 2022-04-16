
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head == None:
            return False
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
