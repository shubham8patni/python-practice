from numpy import number


numbers = [2,5,6,7,3,1,2,8]

def squares(numbers):
    return numbers * numbers

squared_num_iter = map(squares, numbers)

numberlist = list(squared_num_iter)
print(numberlist)