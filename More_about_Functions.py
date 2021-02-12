def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def sub(a, b):
    return a / b


def div(a, b):
    return a / b


def cal(a, b, fn_name):  #this function returns the function name
    return fn_name(a, b)


res = cal(5, 6, add)
print(res)
print(type(cal)) #return type can be functions if it resturns a function object

type(cal(5, 6, fn_name=add))

cal_dic = {"+": add,  #functions can be values of keys for dictionaries
           "-": sub,
           "*": mul,
           "/": div}

res = cal_dic["+"](5, 6)
print(res)

sum=add  #function is assigned to a varaible and the type of function is function
print(type(sum))


