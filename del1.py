# class Human:
#     name="Neeraj"
#     game="Free Fire"
#     def showDetails(self):
#         print(f"Hello {self.name} and my game is {self.game}")

# newBoy=Human()
# # newBoy.name="Manik"
# # newBoy.game="PubG"
# newBoy.showDetails()

class Human:
    def __init__(self,name,game):
        print(self.__dir__())
        self.name=name
        self.game=game
        print(self.__dir__())

    @property
    def getName(self):
        return self.name
    

    @getName.setter
    def getName(self,newName):
        if isinstance(newName, str):
            self.name=newName
        else:
            print("Hello")
        
    
    def showDetails(self):
        print(f"Hello {self.name} and my game is {self.game}")

newBoy1=Human("Neeraj","Hill Climb")
# newBoy2=Human("suman","Manik Babu")
# newBoy1.name="Manik"
# newBoy1.game="PubG"
# newBoy1.showDetails()
# newBoy2.showDetails()
newBoy1.getName="123"
print(newBoy1.getName)
# print()