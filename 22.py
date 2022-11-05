def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('tarakananda',age=20,city='Pulivendula',mob=8374001220)