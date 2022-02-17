
from numpy import append, number


numbers = [2,5,6,7,3,1,2,8]
result = []
def squares(numbers, numbers2, numbers3):
    result.append(numbers * numbers)
    result.append(numbers2 * numbers2)
    result.append(numbers3 * numbers3)
    # num2 = [numbers2 * numbers2]
    # num3 = [numbers3 * numbers3]
    # result.append(num2)
    # result.append(num3)
    #result = numbers + numbers2 + numbers3
    return result

# squared_num_iter = map(squares, numbers)

# numberlist = list(squared_num_iter)
# print(numberlist) 

#multiple iterations : for example we have data input from 4 different pipelines. All this data needs to go thriugh validation check or some other operation (like scaling 1/255) so instead of seperately calling the function for the 4 different inputs or making 4 different functions for each, we can just pass them all through using "map". 

numbers2 = [20,50,60,70,30,10,20,80]
numbers3 = [25,55,65,75,35,15,25,85]

squared_num_iter = map(squares, numbers,numbers2,numbers3)

numberlist = list(squared_num_iter)
print(numberlist[0]) 

# Can be used with lambda too