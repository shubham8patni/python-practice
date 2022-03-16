class Solution:
    def myAtoi(self, s: str) -> int:
        sign = ""
        int1 = ""
        ans = 0
        for i in range(len(s)):
            if s[i]=="1" or s[i]=="2" or s[i]=="3" or s[i]=="4" or s[i]=="5" or s[i]=="6" or s[i]=="7" or s[i]=="8" or s[i]=="9" or s[i]=="0" or s[i]=="+" or s[i]=="-" or s[i]== " ":
                if s[i] == " " and i==0:
                    pass
                elif s[i] == " " and s[i-1]!=" ":
                    break
                elif s[i] == "+" and s[i-1]=="+" and s[i-1]=="-":
                    break
                elif s[i] =="-" and s[i-1]=="+" and s[i-1]=="-":
                    break
                elif s[i] == "+" and s[i-1]!="+" and s[i-1]!="-":
                    sign = "+"
                elif s[i] =="-" and s[i-1]!="+" and s[i-1]!="-":
                    sign = "-"
                
                else:
                    int1 = int1 + s[i]
            else:
                break
                
        if len(int1)==0:
            return 0
        elif len(int1)==1:
            if int1 == "+" or int1=="-":
                return 0
        
        ans = int(sign + int1)
        if ans > 2147483647 :
            return 2147483647
        elif ans < -2147483648:
            return -2147483648
        else:
            return ans
            