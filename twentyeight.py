#queue Using Collections module using appendleft and pop
from collections import *
stack=deque()
def push():
    a=int(input("Enter the element to insert : "))
    stack.appendleft(a)
    print(stack)
def pop_element():
    a=stack.pop()
    print("The deleted element is :",a)
    print("The elements in the stack are : ",stack)
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