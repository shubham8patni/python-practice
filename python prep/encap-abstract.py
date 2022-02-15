def addition(var1: int, var2: int):
    sum = var1 + var2
    return sum

def director(var1: int, var2: int):
    final = addition(var1, var2)
    return final

if __name__ == "__main__" :
    var1, var2 = map(int, input("Enter the numbers for addition : ").split())
    answer = director(var1, var2)
    print(answer)