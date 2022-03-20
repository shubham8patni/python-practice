# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k):
        dum1 = dum2 = head
        counter = 1
        
        if head==None or head.next==None:
            return head
        
        while dum1.next:
            counter +=1
            dum1=dum1.next
        print(counter)
        
        if counter == k:
            return head
        dum1.next = head
        if k<counter:
            ck = counter-k-1
        elif k>counter:
            ck = k%counter
            ck = counter-ck-1
        print(ck)
        for i in range(ck):
            print(ck)
            dum2 = dum2.next
        dum3 = dum2.next
        dum2.next=None
        return dum3
        