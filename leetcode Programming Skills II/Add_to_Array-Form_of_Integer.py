class Solution:
    def addToArrayForm(self, num, k: int) :
        temp = ""
        for i in num:
            temp += str(i)
        
        temp = int(temp)
        temp = temp + k
        temp = list(str(temp))
        return temp
        