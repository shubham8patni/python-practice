# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head, k) :
        if head.next==None:
            return head
        
        
        temp1 = temp2 = temp3 = head   
        
        for i in range(k-1):
            temp1 = temp2 = temp1.next    
        
        while temp2.next:
            
            temp2 = temp2.next
            temp3 = temp3.next
        
        temp1.val, temp3.val = temp3.val,temp1.val
        
        
        return head
    
        