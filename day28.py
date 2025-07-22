# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def greet(self):
#         print(f"Hello {self.name} and age is {self.age}")
    
#     @property
#     def getValue(self):
#         return self.name
    
#     @getValue.setter
#     def setValue(self,name):
#         if(not name.isnumeric()):
#             self.name=name
        

# obj1=Animal("Rat",56)

# # print(obj1.name)  # getting the value
# # obj1.name=5676778  # setting the value

# # print(obj1.getValue) # pythonic way to get a value
# obj1.setValue="Niti" # pythonic way to set a value

# obj1.greet()
class Parent:
    def display(self):
        print("This is Parent class.")
        
class Child(Parent): # Inheriting Parent class
    def show(self):
        print("This is Child class.")  


obj = Child()
obj.display() # Accessing Parent class method
obj.show() # Accessing Child class method