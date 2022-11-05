class Student:
    def __init__(self,name,age,college,Brand,Processor,RAM):
        self.name=name
        self.age=age
        self.college=college
        self.lap=self.Laptop(Brand,Processor,RAM)
    def show(self):
        print(self.name,self.age,self.college)
        self.lap.show()
    class Laptop:
        def __init__(self,Brand,Processor,RAM):
            self.Brand=Brand
            self.Processor=Processor
            self.RAM=RAM
        def show(self):
            print(self.Brand,self.Processor,self.RAM)
student1=Student('Tarakananda Reddy', 20, 'Sree Vidyanikethan Engineering College','HP', 'i7', 16)
student2=Student('Lohitha',20,'Ravindra Degree College','HP', 'i5', 8)
student3=Student('Risheesh',20,'BVRIT College','Dell', 'i7', 16)
student4=Student('B Tharun',20,'NIT Allabad','HP', 'i7', 8)
student1.show()
student1.lap.show()
student2.show()
student2.lap.show()
student3.show()
student3.lap.show()
student4.show()
student4.lap.show()