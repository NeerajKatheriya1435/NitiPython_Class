class Student:
    def __init__(self,name):
        self.name=name
    
    def showName(self):
        print(f"The name is {self.name}")

class UserInput(Student):
    def __init__(self,name,sub1,sub2):
        super().__init__(name)
        self.sub1=sub1
        self.sub2=sub2

    def showMarks(self):
        print(f"The marks of Maths: {self.sub1}")
        print(f"The marks of Physics: {self.sub2}")

class Result(UserInput):
    def __init__(self, name, sub1, sub2):
        super().__init__(name, sub1, sub2)
    
    def myResult(self):
        self.myres=self.sub1+self.sub2
        print(f"My name is {self.name}")
        print(f"My numbers in Maths {self.sub1}")
        print(f"My numbers in physics {self.sub2}")
        print(f"The result is {self.myres}")

obj1=Result("Niti",90,95)
# print(Result.mro())
# obj1.showName()
# obj1.showMarks()
obj1.myResult()

# request module, time module

# a,b,c---d,e---u