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
    sum = 0
    for x in bill:
        if x == bill[k]:
            pass
        else:
            sum += x
    #print(k)
    if sum//2 == b:
        print("Bon Appetit")
        #return "Bon Appetit"
    else:
        print(b - sum//2)
        #return (b-k)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
