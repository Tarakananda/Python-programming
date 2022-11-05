#Operator Overloding
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __gt__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        if m1>m2:
            return True
        else:
            return False
    def __add__(self,other):
        r1=self.m1+other.m2
        r2=self.m2+other.m1
        r3=r1+r2
        return r3
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)
s1=Student(45, 55)
s2=Student(55, 65)
print(s1+s2)
if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")
print(s1)
print(s2)