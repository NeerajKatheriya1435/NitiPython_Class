
# def printName(name):
#     print(name)

# def greet(func1):
#     print("Hello Good Morning")
#     func1("Rahul")
#     print("Bye Bye")

# greet(printName)

def decorator(mfx):
    def newFunc():
        print("-------------")
        mfx()
        print("-------------")
    return newFunc

@decorator
def printName():
    print("Shivam")

printName()