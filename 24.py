def names(lst):
    count=0
    for i in range(10):
        d=len(lst[i])
        if d>5:
            count+=1
    return count
lst=[]
for i in range(10):
    n=input("Enter name {}: ".format(i))
    lst.append(n)
c=names(lst)
print(c)