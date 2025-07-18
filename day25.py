
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def showDetails(self):
        print(f"The name is {self.name} and age is {self.age}")
    
    @property
    def getName(self):
        return self.name
    
    @getName.setter
    def setName(self,name):
        self.name=name

objStd=Employee("Neeraj",56)
# print(objStd.name) // not good practice
# objStd.name="Shubham" // not good practice

print(objStd.getName)
objStd.setName="Gudiya"

objStd.showDetails()