#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    if n%2==0:
        if n-p < p:
            ans = ((n-p-1)/2)+1
        elif n-p > p:
            ans = ((p-1)/2)+1
        elif n-p == p:
            ans = ((p-1)/2)+1
    elif n%2!=0:
        if n-p < p:
            ans = ((n-p-1)/2)
        elif n-p > p:
            ans = ((p-1)/2)
        elif n-p == p:
            ans = ((p-1)/2)
    return int(ans)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
