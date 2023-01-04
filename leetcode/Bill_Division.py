#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    # print(bill, k, b)
    total = 0
    for i in range(len(bill)):
        # print(bill[i])
        if i == k:
            pass
        else:
            total += bill[i]
            # print(total)
    
    if b == total/2:
        print("Bon Appetit")
    else:
        print(int(b - total/2))
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

