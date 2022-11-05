j=input()
x=0
for i in range(len(j)):
    if j[i]=='_':
        x=True
        break;
    else:
        x=False
if x==True:
    print(True)
else:
    print(False)