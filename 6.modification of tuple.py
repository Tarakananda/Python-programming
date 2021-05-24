#tuple cannot be modified directly
atup=(10,20,30,40)
alist=list(atup)
alist[0]=10000
atuple=tuple(alist)
print("elements in the list:",atup)