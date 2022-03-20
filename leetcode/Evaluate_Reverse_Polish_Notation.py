class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":   
                temp = stack[-2] + stack[-1]
                stack.pop()
                stack[-1]=temp
            elif tokens[i] == "-":
                temp = stack[-2] - stack[-1]
                stack.pop()
                stack[-1]=temp
            elif tokens[i] == "*":              
                temp = stack[-2] * stack[-1]
                stack.pop()
                stack[-1]=temp
            elif tokens[i] == "/":                
                if stack[-1]==0 or stack[-2]==0:
                    temp = 0
                elif stack[-2] == stack[-1]:
                    tmp = 1
                else:
                    temp = stack[-2] / stack[-1]
                    temp = int(temp)                
                stack.pop()
                stack[-1]=temp
            else:
                stack.append(int(tokens[i]))
            
        return stack[0]