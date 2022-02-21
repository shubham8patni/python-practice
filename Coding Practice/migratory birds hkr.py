#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    arr.sort()
    print(f"Sorted Array : {arr}\n")
    counter = 0
    dict1 = {}
    if len(arr)==1:
        return arr[0]

    for i in range(len(arr)): 
        if i == 0:
            x = arr[i]
        elif x == arr[i]:
            print(arr[i])
            counter += 1
        else:
            dict1[x] = counter + 1
            counter = 0
            x = arr[i]
    
    v = max(dict1.values())    
    for i,j in dict1.items():    
        if j==v:
            print(i)
            return i
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')
    
    fptr.close()
