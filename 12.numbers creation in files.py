fobj = open(r"D:\python programs\files\2.txt","w")
for val in range(1,100):
    fobj.write(str(val) +"\n")
fobj.close()