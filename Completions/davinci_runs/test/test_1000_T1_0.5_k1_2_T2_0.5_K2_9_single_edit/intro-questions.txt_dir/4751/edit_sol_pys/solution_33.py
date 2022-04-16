# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return 0
        slow = head.next
        fast = head.next.next
        while fast != None and fast.next != None and fast != slow:
            fast = fast.next.next
            slow = slow.next
        if fast == None or fast.next == None:
            return 0
        count = 1
        slow = slow.next
        while slow != fast:
            slow = slow.next
            count += 1
        return count
