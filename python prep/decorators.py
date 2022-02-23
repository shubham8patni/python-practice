# Logging.. you have different actions like login, user creation, document update, you can use decorator to log them all and no need to write the function again and again or rather than chaning code in different files wherever it is needed
# closure : making a function inside a function allowing the inside function to by default inherit variables of outer function without passing them as parameter
# as you can see below we are returning a function itself "inner_func" and storing it in a variable and now the variable itself can be called like a function
from audioop import add
from sys import displayhook


def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

func = outer_func('hello there!!')
func()


a = 10
b = 2
def dec_divide(func):
    def inner(a,b):
        print(f"i am going to divide {a} by {b}")
        if b==0:
            print(f"can't divide a number by 0")
            return

        return func(a,b)
    return inner

@dec_divide
def divide(a,b):
    print(a/b)

divide(a,b)

# Logging.. you have different actions like login, user creation, document update, you can use decorator to log them all and no need to write the function again and again

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level = logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args : {}, and kwargs : {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

@my_logger
def display_info(name,age):
    print('display_info ran with arguements ({}, {})'.format(name, age))

display_info('Shubham', 24)




def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1]) for val in list_of_tuples]
    return inner


@decorator_list
def add_together(a, b):
    return a + b


print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))

# add_together = decorator_list(add_together)
