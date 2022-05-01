class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        newS = []
        for i in s:
            if i == "#":
                if len(newS)==0:
                    pass
                else:
                    newS.pop()
            else:
                newS.append(i)
        
        newT = []
        for i in t:
            if i == "#":
                if len(newT)==0:
                    pass
                else:
                    newT.pop()
            else:
                newT.append(i)
        
        if newS == newT:
            return True
        else:
            return False