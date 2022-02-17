# closure : making a function inside a function allowing the inside function to by default inherit variables of outer function without passing them as parameter
# as you can see below we are returning a function itself "inner_func" and storing it in a variable and now the variable itself can be called like a function
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

# Logging

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