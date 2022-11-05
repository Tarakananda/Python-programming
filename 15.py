class animal:
    def sound(self):
        print('Animal makes sound.')
class Dog(animal):
    def sound(self):
        super().sound()
        print("Dog baraks.")
d=Dog()
d.sound()