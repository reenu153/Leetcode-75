# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head=None
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val<list2.val:
            head=list1
            list1=list1.next
        else:
            head=list2
            list2=list2.next
        
        dup=head

        while(list1 and list2):
            
            if list1.val<list2.val:
                dup.next=list1
                list1=list1.next
            else:
                dup.next=list2
                list2=list2.next

            dup=dup.next

        if list1:
            dup.next=list1
        elif list2:
            dup.next=list2

        return head

        