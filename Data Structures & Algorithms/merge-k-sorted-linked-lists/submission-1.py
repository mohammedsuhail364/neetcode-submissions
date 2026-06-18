# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def __init__(self):
        self.head=None
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        li=[]
        for i in lists:
            while i:
                li.append(i.val)
                i=i.next
        li.sort()
        for i in li:
            self.insert1(i)
        return self.head
    def insert1(self,data):
        if self.head is None:
            self.head=ListNode(data)
            self.temp=self.head
        else:
            self.temp.next=ListNode(data)
            self.temp=self.temp.next