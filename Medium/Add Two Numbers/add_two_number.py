class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode()
        extra = 0

        while l1 or l2:
            a = 0 
            b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val 
                l2 = l2.next 

            total = a + b + extra 
            extra = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next 
            
        if extra:
            curr.next = ListNode(extra)
        
        return dummy.next