class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            val1 = 0
            val2 = 0

            if l1:
                val1 = l1.val
                l1 = l1.next

            if l2:
                val2 = l2.val
                l2 = l2.next

            total = val1 + val2 + carry

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

        return dummy.next
    
# python has built in functions to operate through a nested list. like ( .val, .next)
# in order to get position of a number ie ones tens hundrenths. use position = number % 10 