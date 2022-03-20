class Solution:
    def myPow(self, x: float, n: int) -> float:
        y=x
        if n == 0:
            return 1
        if n>0:
            #for i in range(n-1):
                #y = y*x
            return pow(x,n) #y
        if n < 0:
            #for i in range(n*(-1)-1):
                #y = y*x
            return pow(x,n) #1/y




    #Alternate
        # y=x
        # if n == 0:
        #     return 1
        # if n>0:
        #     for i in range(n-1):
        #         y = y*x
        #     return y
        # if n < 0:
        #     for i in range(n*(-1)-1):
        #         y = y*x
        #     return 1/y