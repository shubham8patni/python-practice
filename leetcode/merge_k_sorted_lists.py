# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists) :
        arr = []
        for i in lists:    
           
            while i:
                arr.append(i.val)
                i = i.next
        arr.sort()
        if len(arr)==0:
            return None
        
        dum1 = head = ListNode(arr[0])
        for i in range(1,len(arr)):
            dum1.next = ListNode(arr[i])
            dum1 = dum1.next
        return head