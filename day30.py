# class Person:
#     def __init__(self,name,rollNum):
#         self.name=name
#         self.rollNum=rollNum

#     def studentDetails(self):
#         print(f"My name is {self.name} and roll number {self.rollNum}")
        
# class Boy(Person):
#     def __init__(self, name, rollNum,language):
#         super().__init__(name, rollNum)
#         self.language=language
    
#     def studentDetails(self):
#         # print(f"Name is {self.name} and language is {self.language}")
#         super().studentDetails()

# Rohan=Boy("Neeraj",101,"English")

# Rohan.studentDetails()

# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return f"Hello my name is {self.name}"

# p = Person("Neeraj")
# # print(p.__dir__())
# print(str(p))

class Person:
    def __init__(self, name,sub1,sub2):
        self.name = name
        self.sub1=sub1
        self.sub2=sub2
    
    def result(self):
        self.sumResult=self.sub1+self.sub2
        print("The result of {self.name} is {self.sumResult}")

    # def ageDetails(self):
    #     print(f"The age issssssssssssss {self.name}")


class Student:
    def __init__(self,age):
        self.age=age
    
    def ageDetails(self):
        print(f"The age is {self.age}")

class Mohan(Person,Student):
    def __init__(self, name, sub1, sub2,age,rollNumber):
        # super().__init__(name, sub1, sub2)
        Person.__init__(self,name, sub1, sub2)
        Student.__init__(self,age)
        self.rollNumber=rollNumber

    def showRoll(self):
        print("The Roll number is {self.rollNumber}")

m1=Mohan("Shubham",51,52,45,1101)

print(Mohan.mro())
m1.ageDetails()