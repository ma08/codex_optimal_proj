#
# class Solution:
#     def canThreePartsEqualSum(self, A) -> bool:
#         total = sum(A)
#         if total % 3 != 0:
#             return False
#         target = total // 3
#         cur = 0
#         count = 0
#         for num in A:
#             cur += num
#             if cur == target:
#                 count += 1
#                 cur = 0
#         return count == 3


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0
        while l1.next:
            num1 = (num1 * 10) + l1.val
            l1 = l1.next
        num1 = (num1 * 10) + l1.val
        while l2.next:
            num2 = (num2 * 10) + l2.val
            l2 = l2.next
        num2 = (num2 * 10) + l2.val
        print(num1, num2)
        sum_ = num1 + num2
        print(sum_)
        res = None
        while sum_ > 0:
            rem = sum_ % 10
            sum_ = sum_ // 10
            if res is None:
                res = ListNode(rem)
            else:
                temp = ListNode(rem)
                temp.next = res
                res = temp
        return res


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()
res = sol.addTwoNumbers(l1, l2)
while res:
    print(res.val)
    res = res.next
