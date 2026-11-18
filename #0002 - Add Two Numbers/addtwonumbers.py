# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        newList = ListNode(0)
        current = newList
        carry = 0
        total = 0
        while l1 or l2 or carry:
            numOne = 0
            numTwo = 0
            if l1:
                numOne = l1.val
            if l2:
                numTwo = l2.val
            total = carry + numOne + numTwo
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return newList.next
