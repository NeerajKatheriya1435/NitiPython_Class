# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def addtwoNumber(self,num1,num2):
#         return num1+num2
    

#     @staticmethod
#     def AddTwoNum(num1,num2):
#         # print(f"my name is {self.name}")
#         return num1+num2

# cat=Animal("Cat",78)

# print(cat.addtwoNumber(7,9)) # not recommnded
# print(cat.__dict__)

# print(Animal.AddTwoNum(7,4))
# print(cat.addTwoNumber(6,9))


# print(Animal.__dir__(cat))
# 
# list1=[6,8,5]

# help(list1.sort)
# help(list1.append)

# class Student:
#     school_name = "Tech Mech Institute"
#     def __init__(self, name):
#         self.name=name
    
#     def chnageDetail(self,updatedName):
#         self.name=updatedName

#     @classmethod
#     def details(cls):
#         cls.school_name="My School"

#     def showDetails(self):
#         self.school_name="GOVT Polytechnic"
#         print(f"Hello {self.name} and my school is {self.school_name}")

# newObj=Student("Niti Tiwari")

# newObj.showDetails()  # "Hello Niti Tiwari and my school is GOVT Polytechnic"
# print(newObj.school_name) # "GOVT Polytechnic"
# print(Student.school_name) # "Tech Mech Institute"

# newObj.details()  
# newObj.showDetails() # # "Hello Niti Tiwari and my school is GOVT Polytechnic"
# print(newObj.school_name)  # "GOVT Polytechnic"
# print(Student.school_name) # "My School"