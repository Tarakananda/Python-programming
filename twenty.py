from collections import defaultdict

d=defaultdict()
n=int(input())
for i in range(n):
    x=input()
    if(x not in d.keys()):
        d[x]=1
    else: 
        d[x]=d.get(x)+1
print(len(d))
for i in d.values(): 
    print(str(i)+' ',end='')