package main

type ListNode struct {
    Val int
    Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    backList := &ListNode{}
    head := backList

    for list1 != nil && list2 != nil{
        if list1.Val <= list2.Val{
            head.Next = &ListNode{Val: list1.Val}
            list1 = list1.Next
        }else{
            head.Next = &ListNode{Val: list2.Val}
            list2 = list2.Next
        }
        head = head.Next
    }

    if list1 != nil{head.Next = list1}
    if list2 != nil{head.Next = list2}

    return backList.Next
}