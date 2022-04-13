# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Algorithm:
1. Create 2 pointers: fast and slow 
2. If fast and slow meet at same node, return True
3. If fast and slow don't meet, return False

T: O(n), S: O(1)
"""

"""
@param {ListNode} head
@return {boolean}
"""
def hasCycle(head):
    if head is None:
        return False

    fast = head.next
    slow = head

    while fast is not None and fast.next is not None and slow is not None:
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next

    return False
