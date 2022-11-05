n=int(input())
lst=[]
lst1=[] 
count=1
for i in range(n):
    a=input()
    lst.append(a)
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j]:
            count+=1
        lst1.append(count)
    count=1
b = list(set(lst))
a=len(b)
print(a)

for i in range(a):
    print(lst1[i],end=" ")
