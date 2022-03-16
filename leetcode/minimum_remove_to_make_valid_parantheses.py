class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lsi = list(s)
        stack = []
        stack1 = []
        for i,ele in enumerate(lsi):                     
            if ele=="(":                
                stack.append(i)
            elif ele==")" and len(stack)>0:                       
                stack.pop()
            elif ele==")" and len(stack)==0:        
                #s = s[:i]+s[i+1:]
                stack1.append(i)
        stack = stack + stack1
        stack.sort()
        stack = stack[::-1]

        for i in stack:
            s = s[:i]+s[i+1:]

        return s