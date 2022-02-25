class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for i in range(len(s)):
            if i == 0:
                a.append(s[i])
            elif len(a)==0 and (s[i]==']' or s[i]==')' or s[i]=='}'):
                return False
            elif (s[i]==')' and a[-1]=='(') or (s[i]=='}' and a[-1]=='{') or (s[i]==']' and a[-1]=='['):
                a.pop()
            else:
                a.append(s[i])
                
        if len(a)==0:
            return True
        else:
            return False

        