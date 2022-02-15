import imp
import numpy as np
from scipy import stats

#MEAN - average of all numbers
#Without Library/Function
array = np.random.randint(150, size=100)
print("random array of size 100 : \n" , array )
sum1 = 0
for number in range(len(array)):
    sum1 += array[number]
    # sum1 = sum(array)

mean = sum1/len(array)
print("Mean without using mean function : \n" , mean)

#With Library/Function

mean2 = np.mean(array)
print("Mean using mean function : \n" , mean2)

print("\n\n\n")

#MODE - number that occurs most
#Without Library/Function
array2 = np.array([5,6,2,7,8,9,3,2,5,6,1,5,5])
print("List of original array: \n " , array2)
#array2.sort() --converts original array
sorted_arr = sorted(array2)
print("Sorted List : \n", sorted_arr)
counter = 0
Dict = {}
for i in range(len(sorted_arr)):
    if i == 0:
        x = sorted_arr[i]
    elif x == sorted_arr[i]:
        x = sorted_arr[i]
        counter += 1
    elif x != sorted_arr[i]:
        Dict[x] = counter
        x = sorted_arr[i]
        counter = 0

v = max(Dict.values())
for key, value in Dict.items():
         if v == value:
             print("Mode without using Mode function : ", key)

#With Library/Function
mode2 = stats.mode(array2)
print("Mode using Mode function : ", mode2)

print("\n\n\n")


#MEDIAN - middle number of the array
#Without Library/Function
array3 = np.array([5,6,2,7,8,9,3,2,5,61,78,20,6,1,5,5,10,5,6,3,7,44])
print("Unsorted array : ", array3)
n = len(array3)
print("Length of array : ", n)
array3.sort()
print("Sorted array : ", array3)
if n%2 == 0:
    print("median without function is :", array3[n//2])
elif n%2 != 0:
    print("median without using function is :", array3[n//2]+1)

#With Library/Function
median = np.median(array3)
print("Median using Meadian function is : ", median)