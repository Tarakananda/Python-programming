class A:
    def __init__(self):
        print("Constructor in Class A")
    def fearure1(self):
        print("This is a feature A-1 Class")
    def fearure2(self):
        print("This is a feature 2 Class")
class B:
    def __init__(self):
        print("Constructor in Class B")
    def fearure1(self):
        print("This is a feature B-1 Class")
    def fearure2(self):
        print("This is a feature 3 Class")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("Constructor in Class C")
    def fearure4(self):
        print("This is a feature 4 Class")
    def fearure5(self):
        print("This is a feature 5 Class")
    def fearure6(self):
        super().fearure2()
c1=C()
c1.fearure1()
c1.fearure6()