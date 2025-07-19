class Employee:
    company="Tesla"
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def details(self):
        print(f"My Name is {self.name} and id is {self.id} company is {self.company}")
    

e1=Employee("Kuamr",1101)
e1.details()
e1.company="Tech-Mech"
# print(e1.company)
e1.details()
Employee.company="Hero"
print(Employee.company)