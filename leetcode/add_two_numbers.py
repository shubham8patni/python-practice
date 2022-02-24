# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def traverse(self, l1):
        list1 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        return list1
        
    def addTwoNumbers(self, l1, l2):
        #dummy acts as header since later in code we use cur to increase linked list, thus cur becomes the linked list and dummy acts as head
        cur = dummy = ListNode(0)
        list1 = self.traverse(l1)
        list2 = self.traverse(l2)
        length = 0
        carry = 0
        res = []
        if len(list1)<len(list2):
            length = len(list2)
            list1.extend([0] * (length - len(list1)))
        else:
            length = len(list1)
            list2.extend([0] * (length - len(list2)))
            
        for i in range(0,length):                
            if list1[i]+list2[i]+carry>9:
                temp = list1[i]+list2[i]+carry
                carry = temp//10
                temp = str(temp)
                res.append(int(temp[1]))
            else:
                res.append(list1[i]+list2[i]+carry)
                carry = 0
        if carry>0:
            res.append(carry)
        
        for i in res:
            cur.next = ListNode(int(i))
            cur = cur.next 
        
        return dummy.next
        