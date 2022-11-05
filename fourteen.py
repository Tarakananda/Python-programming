class Interator:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
s1=Interator()
print(s1.__next__())
for i in s1:
    print(i)