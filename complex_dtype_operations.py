import numpy as np
l1=[10,20,30,40,50]
l1.append([50,60])
l1.insert(30,4)
print(sorted(l1[0:5]))
print(l1)
print(np.array(l1[0:5],dtype="int"))
c=np.arange(0, 10).reshape(2,5)
print(c)

a=np.arange(10,50,2,dtype="int")
print(np.hsplit(a,[8]))

l1=[10,20,30,40]
l2=[4,3,2,1]
arr1=np.array(l1)
print(arr1)