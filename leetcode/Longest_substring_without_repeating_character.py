#check prev
#check next
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #counter = 1
        temp = []
        #temp = ""
        lenar=[]
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        else:      
            for i in range(len(s)):
                if i ==0:
                    #temp = s[i]
                    temp.append(s[i])
                elif s[i] in temp:
                    if s[i]==temp[-1]:
                        lenar.append(len(temp))
                        counter = 1
                        temp = []
                        temp.append(s[i])
                    else:
                        #for j in range(temp.index(s[i]),len(temp)):
                        lenar.append(len(temp))
                        temp = temp[temp.index(s[i])+1::]
                        counter = 1
                        temp.append(s[i])
                else:
                    temp.append(s[i])
                    #counter += 1
        lenar.append(len(temp))
        return max(lenar)
        #print(lenar)       