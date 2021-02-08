from functools import reduce

a=[1,4,3,5,6,74,46,54]
print(a)
odd=list(filter(lambda a:a%2!=0,a))
print("odd list is:",odd)  # filter takes two arguments 1 is function and another is a iterable object here we are using lambda function
double_odd=list(map(lambda a:a+a,odd)) # map will take the filtered output and performs some operation said in the lambda fn
print("double_odd using map function:",double_odd)
double_filter=list(filter(lambda a:a*2,odd))
print("trying to use filter like map but it didn't work:",double_filter)

mul=reduce(lambda a,b:a*b,double_filter)
print("Using the reduce function we are reducing the list into a single number:",mul)
