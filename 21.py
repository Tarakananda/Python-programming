from numpy import *
arr1=array([
        [1,2,3,4,5,3],
        [5,6,7,8,9,5]
        ]
    )
print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
arr2=arr1.flatten()
print(arr2)
arr3=arr2.reshape(4,3)
print(arr3)
m1=matrix('1,2,3;4,5,6;7,8,9')
print(m1)
print(diagonal(m1))