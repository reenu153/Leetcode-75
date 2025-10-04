# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen=[]

        # while(head):
        #     if head.val in seen:
        #         return head
        #     seen.append(head.val)
        #     if head.next==None:
        #         return None
        #     head=head.next


        while(head):
            if head in seen:
                return head
            seen.append(head)
            if head.next==None:
                return None
            head=head.next
        


        