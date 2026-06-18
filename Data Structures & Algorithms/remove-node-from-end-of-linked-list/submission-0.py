# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        li=[]
        while head:
            li.append(head.val)
            head=head.next
        li.pop(-n)
        head=None
        for i in li:
            if head==None:
                head=ListNode(i)
                temp=head
            else:
                temp.next=ListNode(i)
                temp=temp.next
        return head