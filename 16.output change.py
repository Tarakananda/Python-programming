with open(r"D:\python programs\files\realestate.csv","r") as fobj:
    for line in fobj:
        line=line.strip()  #remove white spaces if any
        output=line.split(",")
        print(output[0])
        print(output[1])