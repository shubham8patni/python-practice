class Solution:
    def myAtoi(self, s: str) -> int:
        sign = ""
        int1 = ""
        counter = 0
        for i in s:
            if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i==" " or i=="-" or i=="+":
                if i == " ":
                    if len(int1)>0 or sign!="":
                        break
                    else:
                        pass
                elif i == "-" or i == "+":
                    if sign !="":
                        break
                    if len(int1)>0:
                        break   
                    else:
                        sign = i
                else:
                    int1 += i
            else:
                break
            counter += 1
        
        if int1=="":
            return 0
        
        if sign !="":
            int1 = sign + int1
        
        ans = int(int1)
        if ans > 2147483647 :
            return 2147483647
        elif ans < -2147483648:
            return -2147483648
        else:
            return ans
