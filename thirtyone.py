from queue import *
queue=PriorityQueue()
def push():
    a=int(input("Enter the element to insert : "))
    queue.put(a)
def pop_element():
    a=queue.get()
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