def num_id1(L1,L2):
    L1.extend(L2)
    L1.sort()
    return list(set(L1))
T=int(input("Enter the list of elements : "))
while(T):
    L1=list(map(int, input("Enter the elements in L1").split(",")))
    L2=list(map(int, input("Enter the elements in L2").split(",")))
    print(num_id1(L1,L2))
    T-=1


#Unioun and do intersection