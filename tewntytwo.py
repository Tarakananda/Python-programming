#Stack using list
stack=[]
def push():
    a=int(input("Enter the element : "))
    stack.append(a)
    print(stack)
def pop_element():
    if len(stack)==0:
        print("stack is empty")
    else:
        a=stack.pop()
        print("Removed element ",a)
        print(stack)
while True:
    print("Select the operation 1.push 2.pop 3.exit :")
    choice =int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice ==3:
        break
    else:
        print("Select the correct operation")