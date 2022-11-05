def Largest(n,L):
    for i in range(n):
        L[i]=int(input("Enter an element : "))
    temp=0
    for i in range(n):
        for j in range(n-i):
            if L[i]<L[j]:
                temp=L[i]
                L[i]=L[j]
                L[j]=temp
    for i in range(n):
        print(L[i])
n=int(input("Enter the number of elements : "))
L=[0]*n
Largest(n, L)