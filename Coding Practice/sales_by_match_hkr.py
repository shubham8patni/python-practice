#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    ar.sort()
    list1 = []
    counter = 0
    for i in range(len(ar)):
        if i == 0:
            list1.append(ar[i])
        else:
            if len(list1)==0:
                list1.append(ar[i])
            elif list1[-1] == ar[i]:
                list1.pop()
                counter += 1
            else:
                list1.append(ar[i])
    
    return counter
                
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
