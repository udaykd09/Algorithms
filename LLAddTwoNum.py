# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_list(self):
        while self:
            print self.val,
            self = self.next
        print

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(0)
        temp = head
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            temp.next = ListNode(carry%10)
            carry /= 10
            temp = temp.next
        return head.next

l1 = ListNode(2)
l2 = ListNode(4)
l1.next = ListNode(3)
l2.next = ListNode(5)
l1.next.next = ListNode(7)
l2.next.next = ListNode(9)

l1.print_list()
l2.print_list()
mySol = Solution()
l3 = mySol.addTwoNumbers(l1, l2)
l3.print_list()