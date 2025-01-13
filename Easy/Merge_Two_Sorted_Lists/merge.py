from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.sortedl(list1, list2)
    

    def sortedl(self, list1: ListNode, list2: ListNode) -> ListNode:
        back_list = ListNode()
        head = back_list

        while list1 and list2:
            if list1.val <= list2.val:
                head.next = ListNode(list1.val)
                list1 = list1.next
            else:
                head.next = ListNode(list2.val)
                list2 = list2.next
        
            head = head.next

        if list1:
            head.next = list1
        if list2:
            head.next = list2

        return back_list.next