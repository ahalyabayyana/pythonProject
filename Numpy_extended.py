from numpy import *

a = array([1, 2, 3, 4], dtype="U")  # dtype = u specifies it is a unicode strig of charachters
print("Array a is:", a)
print("Type of data in array can be found by dtpype function", a.dtype)
print("datatype of array from string to int can be change with a.astype function:", a.astype("int"))
b = a.reshape(2, 2)
print("reshaping into array of 1,4  into a array 2,2:", b)
print("shape of array:", b.shape)
print("dimension of array:", b.ndim)
c = arange(1, 10, 1)
print("range of numbers using arange:", c)
print(c.reshape(3, 3))
d = linspace(1, 15, 20, dtype="int")
print("creating array with line space func:", d)
e = logspace(1, 20, 30, dtype="float")  # log means 1 to the power of 20 to 20 to the power of 20
print("creating the array with logspace fn:", e)
l1 = [(12, 13, 14), (23, 24, 25)]
a1 = asarray(l1, order="F")
print("Converting the data l1 into array object using asarray", a1)
for i in iter(a1):
    print(i)
    print()
print("shape of array after converting", a1.shape)
s = b'hello world'
a2 = frombuffer(s, dtype='S1', count=5, offset=6)
print("FRom buffer output with returning 5 characters and starting from 6is:",a2)
a3=fromiter(a,dtype="int")
print(a3)
#copyinh the array
arr1=a1.copy(order="F")
print("a1:",a1)
print("Copy of a1 arr1 is new array the chnages made in one array will not reflect in another array:",arr1)
arr2=a1.view()
print("View is a virtual image of array the chnges done in 1 view will reflect in another:",arr2)


# joining two arrays

def array_join(a,b):

    c=concatenate((a,b),axis=0)
    print("Concatinating a and b with column axis 0 is:\n",c)
    d=concatenate((a,b),axis=1)
    print("Concatinating a and b with row axis 1 is:\n",d)
    e=hstack((a,b))
    print("concatinating with axis 1 i.e with row is hstack:\n",e)
    f=vstack((a,b))
    print("concatinating with axis 0 i.e with column is vstack:\n",f)
    g=stack((a,b),axis=1)
    print("concatinating into 2d array with interms of axis 1 which is row is stack:\n",g)
    h=stack((a,b),axis=0)
    print("Concatinating into 2d array with respect to columns i.e with axis 0 is:\n",h)
    i=dstack((a,b))   #dstack and stack are work opposite way
    print("Concatinating into 2d array with respect to depth :\n",i)



a=arange(8).reshape(2,4)
print("a array is:\n",a)
b=arange(9,17).reshape(2,4)
print("b array is:\n",b)
array_join(a,b)