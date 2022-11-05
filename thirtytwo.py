queue=[]
def push():
    b=input("Enter the string element :")
    a=int(input("Enter the proriety of string to insert : "))
    queue.append((a,b))
    queue.sort()
    print(queue)
def pop_element():
    a=queue.pop()
    print("The deleted element is :",a)
while True:
    print("Select the operation to perform 1.push 2.pop 3.exit :")
    choise=int(input())
    if choise==1:
        push()
    elif choise==2:
        pop_element()
    elif choise == 3:
        break
    else:
        print("Enter the correct operation")