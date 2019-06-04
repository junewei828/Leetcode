# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str_l1, str_l2 = '', ''

        while l1:
            str_l1 += str(l1.val)
            l1 = l1.next
        while l2:
            str_l2 += str(l2.val)
            l2 = l2.next

        int_l1 = int(str_l1[::-1])
        int_l2 = int(str_l2[::-1])
        return list(map(int, str(int_l1 + int_l2)[::-1]))


"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""