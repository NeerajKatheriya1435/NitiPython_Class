class Human:
    # def __init__(self,name,age):
    def __init__(self):
        self.name="name"
        self.age="age"  
        

    def showDetail(self):
        print(f"The name is {self.name} and age is {self.age}")

# obj1=Human("Bhuvan",45)
obj1=Human()
# obj1.name="Rakesh"
obj1.showDetail()

# obj2=Human("Niti",89)
# obj2.showDetail()