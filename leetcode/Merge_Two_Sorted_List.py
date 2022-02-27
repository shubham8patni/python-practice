#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x=[]
        while list1:
            x.append(list1.val)
            list1 = list1.next
        while list2:
            x.append(list2.val)
            list2 = list2.next
        if len(x)==0:
            return 
        x.sort()
        dumm = head = ListNode(x[0])
        for i in range(1, len(x)):
            dumm.next = ListNode(x[i])
            dumm = dumm.next
        
        return head
            