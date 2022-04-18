"""
Algorithm:
1. Create 2 pointers: fast and slow
2. If fast and slow meet at same node, return True
3. If fast and slow don't meet, return False

T: O(n), S: O(1)
"""

"""
@param head {ListNode}
@return {boolean} result
"""
def hasCycle(head):
    if head == None:
        return False

    fast = head.next
    slow = head

    while fast != None and fast.next != None and slow != None:
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next

    return False
