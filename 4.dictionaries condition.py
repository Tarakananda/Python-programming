#dictionary

adict={"chap1":10,"chap2":20}
adict["chap3"]=30
adict["chap4"]=40
print(adict)                        #appending a single element

print("onlykeys:",adict.keys())     #for only keys
print("onlyvalues:",adict.values()) #for only values
print("key-value pairs:",adict.items()) #for both keys and values
print(adict["chap1"])               #to print a single chap
print(adict.get("chap100"))         #to escape from error
adict.pop("chap1")                  #removing the paricular element
print("afterpop:",adict)            
print(adict.popitem())              #will remove random key value pairs(perminently pairs)
print(adict)

book1={"chap1":10, "chap2":20}      #for adding two dictionaries
book2={"chap3":30, "chap4":40}
final={**book1,**book2}
print(final)

book1.update(book2)                 #modifing book1 but indirectely adding dictionaries
print(book1)


#**-dictionaries
#*-tuple