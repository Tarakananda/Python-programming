import csv
with open("D:\\python programs\\files\\realestate.csv","r") as fobj:
    reader= csv.reader(fobj)
    for line in reader:
        print(line)
#each line will be converted to list automatically
#fobj is file object to csv object

