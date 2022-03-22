class Solution:
    def plusOne(self, digits):
        st = ""
        for i in digits:
            st += str(i)
        
        st = str(int(st) + 1)

        ans = []
        for j in st:
            ans.append(int(j))
                
        return ans