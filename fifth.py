class Computer():
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def conf(self):
        print("The conf is :",self.cpu,self.ram)
com1=Computer('i7',16)
com2=Computer('i5',8)
com1.conf()
com2.conf()