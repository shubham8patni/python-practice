import random
import numpy as np
#random.seed(2)

print(random.random())

#generate random matrix
array = np.random.randint(40,size = (4,4))
print(array)

# shuffle 
mylist = [5,5,6,9,7,22,22,4,3,7]
random.shuffle(mylist)
print(mylist)

# Random integer in range ()
# randrange does same as randint
print(random.randint(5,20))


# choices returns list of elements selected randomly, random list can be bigger than original list
mylist1 = ["apple", "banana", "orange", "cherry", "watermelon" ]
print(random.choices(mylist1,weights = [8,1,1,2,4], k = 14))

# choice returns random element from list
print(random.choice(mylist1))