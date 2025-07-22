class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def showDetails(self):
        print(f"The name is {self.name} and age is {self.age}")
    
p1=Parent("Parent",80)
p1.showDetails()

class Child(Parent):
    def __init__(self, name, age,lang):
        super().__init__(name, age)
        self.lang=lang

    def showDetails(self):
        print(f"Name is {self.name} and age {self.age} and lang {self.lang}")
        super().showDetails()

    
c1=Child("Ayush",45,"English")
c1.showDetails()
