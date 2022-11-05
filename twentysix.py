#queue using list enter from front
queue=[]
def enque():
    a=int(input("Enter the element : "))
    queue.insert(0,a)
    print(queue)
def deque():
    if len(queue)==0:
        print("stack is empty")
    else:
        a=queue.pop()
        print("Removed element ",a)
        print(queue)
while True:
    print("Select the operation 1.enque 2.deque 3.exit :")
    choice =int(input())
    if choice == 1:
        enque()
    elif choice == 2:
        deque()
    elif choice ==3:
        break
    else:
        print("Select the correct operation")