# class Employee:
#     company="Tesla"
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
     
#     def details(self):
#         print(f"My Name is {self.name} and id is {self.id} company is {self.company}")
    

# e1=Employee("Kuamr",1101)
# e1.details()
# e1.company="Tech-Mech"
# # print(e1.company)
# e1.details()
# # Employee.company="Hero"
# print(Employee.company)

class Employee:
    company="Tesla"
    def __init__(self,name,id,lang):
        self.name=name # public variable
        self.__id=id  # private variable
        self._lang=lang # protected
     
    def details(self):
        print(f"My Name is {self._lang} and id is {self.__id} company is {self.company}")


emp1=Employee("Shubham",45,"English")
# print(emp1._Employee__id)
# emp1.details()
# print(emp1.name)
# print(emp1._lang)

# print(Employee.__dir__())