#list
alist= [10,20,30,40]
alist.append(60)                    #it adds the element
print(alist)
alist.extend([50,70,80,90])         #it adds multiple elements into list
print(alist)                        
alist.insert(0, 50)                 #it adds the element in specified position
print(alist)                       
alist.pop(1)                        #it will delete the element
print(alist)                        
alist.remove(30)                    #it removes the list when element is specified
print(alist)
alist.reverse()                     #it reverse the list
print(alist)
alist.sort()                        #it modifies the list in assending order
print(alist)
getcount= alist.count(50)
print("count of 50:",getcount)
alist.sort(reverse=True)            #it modifies the list in decending order
print(alist)
name= "sree, vidyanikethan, tharak, lohitha"
print(name.split(":"))              #it converts string into list and it is used to convert string into list
list=["lohitha", "tharak", "sreevidyanikethan"]
print("-".join(list))


#tuple
atup=(10,20,30,30)
print(atup.count(30))


