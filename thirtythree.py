class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_list():
    def __init__(self):
        self.head=None
    def print__LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
s=Linked_list()
while True:
    choise=int(input("Enter 1 to insert more elements, to exit print any number other than 1 : "))
    if choise is 1:
        a=int(input())
        s.add_end(a)
    else:
        break
s.print__LL()