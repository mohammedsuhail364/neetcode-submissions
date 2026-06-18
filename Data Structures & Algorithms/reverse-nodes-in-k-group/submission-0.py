# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        li=[]
        while head:
            li.append(head.val)
            head=head.next
        print(li)
        res=[]
        i=0
        while i<len(li):
            s=li[i:i+k]
            if k==len(s):
                rev=s[::-1]
            else:
                rev=s
            res+=rev
            i+=k
        head=None
        for i in res:
            if head==None:
                head=ListNode(i)
                temp=head
            else:
                temp.next=ListNode(i)
                temp=temp.next
        return head