def add(a, b):
    """This is used to add the two integers"""
    c = a + b
    print("result is ", c)


  # this is used to get the documented part in the functions


def sub(c, d):
    # Here i am using hash symbol to document the comments of code
    """this is for subtracting two numbers"""
    e = c - d
    print("The result of sub is :", e)






def main():
    if(__name__=="__main__"):
        sub(10, 4)
        add(5, 6)
        print(sub.__doc__)
        print(add.__doc__)

main()