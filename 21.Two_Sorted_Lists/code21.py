#21. 合并两个有序链表
#21. Merge Two Sorted Lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #第一种情况是l1为空，合并后的有序链表是l2
        if l1==None:
            return l2
        #第二种情况是l2为空，合并后的有序链表是l2
        elif l2==None:
            return l1
        #第三种情况是l1和l2都为空，返回None
        elif l1==None and l2==None:
            return None
        #如果l1和l2都不为空
        if l1 and l2:
            #如果l1的链表头大于l2的链表头，将l1和l2互换，所以l1的链表头始终是最小的
            if l1.val > l2.val: 
                l1, l2 = l2, l1
            #新的链表还是l1.next，指针指向l1.next和l2
            l1.next = self.mergeTwoLists(l1.next, l2)
        #如果l1的链表头大于l2的链表头，将l1和l2互换，否则的话不用调换，所以l1的链表头始终是最小的，最终得到的新的链表一直都是l1
        return l1 
