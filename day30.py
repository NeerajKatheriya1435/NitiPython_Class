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

class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Hello my name is {self.name}"

p = Person("Neeraj")
# print(p.__dir__())
print(str(p))

