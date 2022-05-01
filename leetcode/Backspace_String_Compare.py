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
        
        print(newS)