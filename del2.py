class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def printName(self):
        print(f"Hello Sir {self.name}")

    def printAge(self):
        print(f"My Age {self.age} and")


class Manager(Employee):
    def __init__(self, name, age,manikRam):
        super().__init__(name, age)
        self.manikRam=manikRam
    def showDetails(self):
        print(f"Hello My age is Java and name is {self.name} and {self.manikRam}")

emp1=Employee("Neeraj",22)
emp1.printAge()
emp2=Manager("Baby",22,"MANIAC")
emp2.showDetails()
# emp1.printAge()