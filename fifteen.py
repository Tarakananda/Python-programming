from abc import ABC, abstractclassmethod
class func(ABC):
    @abstractclassmethod
    def process():
        pass
class func1(func):
    def process():
        print("I am in class func1")
class func2(func):
    pass
s1=func2
s1.process