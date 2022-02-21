#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s.replace(" ","")
    L = len(s)
    ll = math.floor(math.sqrt(L))
    ul = ll + 1
    mat = []
    list1 = []
    j = 0
    
    for i in range(math.ceil(L/ul)):
        m = ""
        for k in range(ul):
            
            if j >= L:
                m += " "
            else:
                m += s[j]
            j += 1
        
        mat.append(list(m))
    k = 0   
    result = ""
    print(mat)
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            if mat[j][i] == " ":
                result += ""
            else:
                print(f"{k}")
                print(str(mat[j][i]))
                result += str(mat[j][i])
                
            k += 1
        result += " "
        
        
    print(result)    
    return result
    
    # for j in range(L):
    #     if j==0:
    #         m += s[j]
    #     elif j%ul != 0:
    #         if s[j] == "" or s[j]==None:
    #             m += ""
    #         else:
    #             m += s[j]
    #     elif j%ul == 0:
    #         m += s[j]
    #         mat.append(list[m])
    #         m = ""
    # print(mat)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny"

    result = encryption(s)

    #fptr.write(result + '\n')

    print("wmgjpnull cyjqlejgi lyhhdzbui wctlsqsbm fxeoxmsvv ovxjeirfm zadysxbhn nxkkbffpn bawobphfy\n" )
    print(result)


    #fptr.close()
