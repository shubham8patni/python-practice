import numpy as np


# 2D array

arr1 = np.array([[1,2,3],[7,8,9]])
arr2 = np.array([[4,5,6],[3,6,9]])
#prints entire array
print("simple print : \n", arr1)

# prints 1D array as elements
for ele in arr1:
    print("single 'for loop' element print",ele)

for x in range(len(arr1)):
    print("single 'for loop' taking x in range (index number) : ", arr1[x])

# print each element using 2 for loops

for x in arr1:
    for y in x:
        print("nested 'for loop' every element print seperately : ", y)

for x in np.nditer(arr1):
    print("print every element using 'nditer function' : ", x)


# Addition of Matrices

print(f"arr1 : \n {arr1} \n arr2 : \n {arr2}")
result  = arr1 + arr2
print("sum : \n", result)

# Multiplication of 2D Matrices

result2 = arr1 * arr2

print("multiply : \n", result2)


#multiplication of 3D matrices 3 * 4

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result3 = [[0,0,0,0,],[0,0,0,0],[0,0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result3[i][j] += X[i][k] * Y[k][j]

print(result3)


#generate random matrix
array = np.random.randint(40,size = (4,4))
print(array)