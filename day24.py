
# def printName(name):
#     print(name)

# def greet(func1):
#     print("Hello Good Morning")
#     func1("Rahul")
#     print("Bye Bye")

# greet(printName)

# def decorator(mfx):
#     def newFunc():
#         print("-------------")
#         mfx()
#         print("-------------")
#     return newFunc

# @decorator
# def printName():
#     print("Shivam")

# printName()

# def addTwoNumber(num1,num2):
#     print("The sum is:",(num1+num2))

# def decoratoWithout(func1):
#     print("Good Morning")
#     func1(2,6)
#     print("Function Finished")

# decoratoWithout(addTwoNumber)

def decoratorNiti(func1):
    def modifiFunc(*args):
        print(*args)
        print("Good Morning")
        func1(*args)
        print("Function Finished")
    return modifiFunc

@decoratorNiti
def addTwoNumber(num1,num2):
    print("Niti Kyumari",(num1+num2))

# decoratorNiti(addTwoNumber(7,4))
# addTwoNumber(5,3)

