# Solution 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        ll = str(x)
        
        if len(ll)%2==0:
            temp = ll[len(ll)//2:]
            temp = temp[::-1]
            if ll[:len(ll)//2]==temp:
                return True
    
        else:
            temp = ll[(len(ll)//2)+1:]
            temp = temp[::-1]
            if ll[:(len(ll)//2)]==temp:
                return True
            




# Solution 2 LOLLL
class Solution:
    def isPalindrome(self, x: int) -> bool:
        ll = str(x)
        
        temp = ll[::-1]
        if ll==temp:
            return True