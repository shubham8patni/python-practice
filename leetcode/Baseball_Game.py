class Solution:
    def calPoints(self, ops) -> int:
        x = []
        for i in ops:
            if i == "D":
                x.append(2*x[-1])
            elif i == "C":
                x = x[:-1]
            elif i == "+":
                x.append(x[-1]+x[-2])
            else:
                x.append(int(i))
        total = sum(x)        
        return total  