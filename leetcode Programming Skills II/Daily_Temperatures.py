class Solution:
    def dailyTemperatures(self, temperatures) :
        stack=[]
        ans=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while len(stack)!=0 and  stack[-1][0]<t:
                stackt,stackInd=stack.pop()
                ans[stackInd]=(i-stackInd)
            stack.append([t,i])
        return ans
                