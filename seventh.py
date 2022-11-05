class Student():
    collegename="Sree Vidyanikethan Engineering College"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value
    @classmethod
    def info(cls):
        cls.collegename="Mohan Babu University"
        return cls.collegename
    @staticmethod
    def info1():
        print("This is Mohan Babu Unversity Erstwhile Sree Vidyanikethanb Engineering College")
student1=Student(30, 40, 50)
student2=Student(60, 70, 80)
student3=Student(80, 90, 100)
print(student1.avg())
print(student1.get_m1())
student1.set_m1(90)
print(student1.avg())
print(student1.get_m1())
print(Student.info())
print(Student.collegename)
Student.info1()
