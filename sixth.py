class person():
    def __init__(self):
        self.name="Kaatutha"
        self.work="poora lamba daltha"
    def update(self):
        self.work="dalega dalega lamba"
    def compare(self,me):
        if self.work==me.work:
            return True
        else:
            return False
poora=person()
lamba=person()
if poora.compare(lamba):
    print("Both are Lamba")
else:
    print("Kaatutha is poora lamba")
print(poora.name)
print(lamba.name)
print(poora.work)
print(lamba.work)
poora.update()
print(poora.work)