#set
aset={10,20,30,20}
bset={30,40,50}
print(aset.union(bset))
print(aset.intersection(bset))
print(aset.issubset(bset))
print(aset.issuperset(bset))
aset.add(90)
print("after addition:",aset)
