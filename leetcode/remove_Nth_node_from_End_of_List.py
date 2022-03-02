# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int) :
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        if len(ans)==1 and n >= 1:
            return
        else:
            num = 0-n
            del ans[num]
            print(ans)
            head = dum = ListNode(ans[0])
            for i in range(1,len(ans)):
                dum.next = ListNode(ans[i])
                dum = dum.next
            
        return head
            