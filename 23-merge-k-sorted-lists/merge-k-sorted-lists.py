# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or not len(lists):
            return None

        while len(lists)>1:
            mergedLists=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                mergedLists.append(self.mergeTwo(l1,l2))
            lists=mergedLists
        return lists[0]
            


    def mergeTwo(self,list1,list2):
        head=ListNode()
        
        if not list1:
            return list2
        if not list2:
            return list1
        
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

        return head.next
        