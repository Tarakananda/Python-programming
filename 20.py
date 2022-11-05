from numpy import *
arr1 =array([1,2,3,4])
print(arr1)
arr2 =arr1
print(id(arr1))
print(id(arr2))
arr3=arr1.view()
print(id(arr1))
print(id(arr3))
arr3[1]=7
print(arr3)
print(arr1)
arr4=arr1.copy()
print(id(arr1))
print(id(arr4))
arr4[2]=8
print(arr1)
print(arr4)