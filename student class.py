class Student():
    def __init__(self,n,a,g,h):
        self.name = n
        self.age = a
        self.grade = g
        self.house = h
    def display(self):
        print(self.name)
        print(self.age)
        print(self.grade)
        print(self.house)

Virnika = Student("Virnika",15,12,"1023DL")
Dhruv = Student("Dhruv",12,8,"1168GK")

print(Dhruv.name)
print(Virnika.name)
Virnika.display()