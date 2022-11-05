def num_id(ip_li):
    L1=[]
    L2=[]
    for i in ip_li:
        if i%2==0:
            L1.append(i)
        else:
            L2.append(i)
    print("Even.",L1)
    print("Odd",L2)
T=int(input("Enter the num of elements : "))
while(T):
    li=list(map(int,input("Enter the list elements : ").split(",")))
    num_id(li)
    T-=1