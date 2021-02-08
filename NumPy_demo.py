import numpy

a = numpy.array([1, 2, 3])
print(a)
print("dimension of a is", a.ndim)
print("shape of a is", a.shape)
print("Type of a is:", type(a))
b = numpy.array([[[1, 2, 3], [3, 4, 5]], [[5, 6, 7], [7, 8, 9]]])
print(b)
print("Dimension of b is", b.ndim)
c = numpy.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]], [[4, 5, 6], [2, 3, 4], [1, 2, 3]]])
print(c)
print("Dimension of c is", c.ndim)
print("shape of c is", c.shape)

a = numpy.zeros((3, 4), dtype="int")
print("prints array of size mentioned with zeros as it is a zeros method",a)
b = numpy.full((2,3),7)
print("Full method is used to fill the array of size mentioned into the number mentioned after the size",b)
c = numpy.eye(4)
print("Eye method is used to print a square matrix with diagonal values equal to 1",c)

d = numpy.arange(1, 9, 1 )
print("creates a array with range of 1 and 9 with step size of 1",d)
print("To get the shape of d",numpy.shape(d))
e = numpy.reshape(d, (2, 4))
print("Reshaping the array into 2 index and 4 items inside each index",e)

f=numpy.reshape([1,2,3,4,5,6,7,8],(4,2))
print("Reshaping the size of f with 4 indexes and 2 items inside it",f)
print("Total number of elements can be found by size function",numpy.size(f))

print("Creating the array with all ones in it",numpy.ones((4,4)))

a=numpy.arange(10,50,2,dtype="int")
print("creating the array with range from 10 to 50 with a stepsize of 2 and returning int datatype",a)
b=numpy.linspace(1,10,20,dtype="int")
print("Creating the array with linespace having index from 1 to 10 and need to return 20items in int datatyep",b)
c=numpy.logspace(1,20,25,base=3,dtype="int")
print("Creates the array with range 1 and 10 with 25 items inside array with base of log(n) with integer data type",c)

#lets see how to retreive the items of array

a=numpy.array([[10,20,3,4,],[2,3,4,5]])
print(a)
print("inorder to retrieve the 0 index and 2 item a[0][2]:",a[0][2])
b=numpy.array([[[10,20,30,40],[2,3,4,5]],[[1,2,3,4],[7,8,9,10]]])
print("Three dimensional array:",b)
print("Retrieving b[-1][1][-3]:",b[-1][1][-3])

#we are using the slicing to retrieve a list of values:

var = a[0, 1:3]
print("Retreving the 0 index array with numbers from 1 to 3:",var)
var1=a[0:2,1:3]
print("retreiving the two indexes and in that retreiving the 1 and 2 items :",var1)
var=b[1,1,1:3]
print("b[1,1,1:3]:",var)
var=b[0:2,0:2, :3]
print(var)

#using the where function to find the item in the array the expression can be anythin

print("prints the element index in array b with value of 40:",numpy.where(b==40))
print("to print all the even numbers in the array:",numpy.where(b%2==0))
#print(numpy.searchsorted(b,25))

#performing the sort on array based on axis,if axis=0 (column sort) ,axis=1 (row_sort)

print(b)

print("Sorted output based on columns is \n",numpy.sort(b,axis=0))

x=numpy.dtype([("name","S10"),("rollno",int)])

student_info=numpy.array([("rekha",16),("kiran",21),("ritvik",13)],dtype=x)
print("Sorted order is:",numpy.sort(student_info,order="rollno"))

#performing arthametic operations on arrays

#1.shape of array's should be same
#2.dimension of array and shape of array should be same
#3.Second array should have only one item

a=numpy.array([[10,20,30],[40,50,60]])
b=numpy.array([[1,2,3],[4,5,6]])
print(a)
print(b)
c=numpy.add(a,b)
print(c)
d=numpy.subtract(a,b)
print(d)
e=numpy.multiply(a,b)
print(e)
f=numpy.mod(b,a)
print(f)
x=numpy.array([10,20,30])
y=numpy.array([[1,2,3],[4,5,6]])
print(x.shape)
print(x.ndim)
print(y.shape)
print(y.ndim)

z=numpy.add(x,y)
print(z)

a=numpy.array([30])
b=numpy.array([[12,13,14,15],[1,2,3,4]])
print(numpy.add(a,b))
print(numpy.power(b,3))


