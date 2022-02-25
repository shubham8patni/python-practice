#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def to_list(self,head):
        ll = []
        while head:
            ll.append(head.val)
            head = head.next
        return ll
    
    def to_link(self,a):
        dummy = head1 = ListNode(a[0])
        for i in range(1,len(a)):
            dummy.next = ListNode(a[i])
            dummy = dummy.next
        return head1
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        a = self.to_list(head)
        a.sort()
        b = self.to_link(a)
        return b