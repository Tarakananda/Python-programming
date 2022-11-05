a=10
def globe():
    a=5
    b=globals()['a']
    print('inside',a)
    globals()['a']=15
globe()
print('outside',a)