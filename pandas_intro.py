from pandas import *

l1=[("Rekha","kiran","ritvik","Pranav"),(401,402,403,404)]
l2=["rekha","kiran","ritvik","pranav"]
d1=DataFrame(l1)
d2=Series(l2)
print("DAta frame can accept 2d array or list of tuples",d1)
print("returns the shape of it as 2d with 4 objects in it",d1.shape)
print("one dimensional array with 4 objects in it",d2.shape)
print("Series can accept only 1d array or list:\n",d2)
print("size of d1 i.e total number of objects present in d1 is",d1.size)
print("size of d2 i.e total number of objects present in d2 is",d2.size)
print("prints the dimensions of d1 array",d1.ndim)
print("prints the dimension of d2",d2.ndim)
#reading data from external csv file
#we have to give double slash to read the file from esires location\\"
data1=read_csv("C:\\Users\\ahaly\\OneDrive\\Desktop\\marks.csv")
df1=DataFrame(data1)
print(df1)