class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
    
        if len(string)==1:
            return x
        elif string[0]=="-":
            string = string[1::]
            string = "-" + string[::-1]
            if int(string)<(-2147483648):
                return 0
            else:
                return int(string)
        else:
            string = string[::-1]
            if int(string)>(2147483647):
                return 0
            else:
                return int(string)
        