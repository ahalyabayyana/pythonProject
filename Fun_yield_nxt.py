import numpy as np
def add(*var):
    for i in var:
        yield i%2
var=np.arange(0,1000,1)
add_gen=add(var)
# print("printing the output using next method",next(add(var)))
# print("Converting into a list :",list(add_gen))


def outer_fn(var):
    print("Welcome to outer function")
    def inner_fn():
        print("Welcome to inner function",var)
    inner_fn()
outer_fn("varaiable is hello")

def outer_fn1(var):
    print("Welcome to outer function",var)
    def inner_fn1(var1):
        print("inner function varaibale:",var1 + "outer function varaiable is :",var)
    return inner_fn1

fn_var=outer_fn1("var is outer")
print(fn_var("var is for inner fn"))