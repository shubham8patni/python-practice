# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        if head==None or head.next == None:
            return head
        elif head.val==head.next.val and head.next.next==None:
            return None
        else:
            while head.next:
                list1.append(head.val)
                head = head.next
            list1.append(head.val)  
            list2 = list1
            list3=[]
            for i in range(len(list1)-1):                
                if list1[i]==list1[i+1]:
                    list3.append(list1[i])
                    
            for i in list3:
                while list2.count(i) != 0:
                        list2.remove(i)
    
            if len(list2) == 0:
                return None
            head2 = dum = ListNode(list2[0])
            for i in range(1,len(list2)):
                dum.next = ListNode(list2[i])
                dum = dum.next

            return head2