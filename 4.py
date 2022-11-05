def Largest(ip_pi,x):
    if x<max(ip_pi):
        return True
    else:
        return False
T=int(input())
while(T):
    li=list(map(int,input().split(",")))
    print(li)
    v=int(input())
    print(Largest(li,v))
    T-=1