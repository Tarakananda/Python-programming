class A:
    def fearture1(self):
        print("Fearure 1 is Working")
    def fearture2(self):
        print("Fearure 2 is Working")
class B:
    def fearture3(self):
        print("Fearure 3 is Working")
    def fearture4(self):
        print("Fearure 4 is Working")
class C(A,B):
    def fearture5(self):
        print("Fearure 5 is Working")
    def fearture6(self):
        print("Fearure 6 is Working")
a1=A()
b1=B()
c1=C()
a1.fearture1()
a1.fearture2()
b1.fearture3()
b1.fearture4()
c1.fearture1()
c1.fearture2()
c1.fearture3()
c1.fearture4()
c1.fearture5()
c1.fearture6()