class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        temp = []
        s = 0
        
        for i in pushed:
            temp.append(i)
            #print(temp)
            while len(temp)>0 and temp[-1]==popped[s]:
                temp.pop()
                s += 1
        
        if len(temp) == 0:
            return True
        else:
            return False