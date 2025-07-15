f=open("data.txt","r+")

# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)

# list1=["Suman\n","Kumar\n","Hardik"]
# f.writelines(list1)
# f.write("Hello Bhai aksie ")
# f.close()
# f.seek(10)
# content=f.readline()
# print(content)
# counter=f.tell()
# print(counter)

# f.write("Hello suman kaisi ho")
# f.truncate(5)

# def addTwoNumber(num1,num2):
#     return (num1+num2)

# var1=addTwoNumber(3,7)
# print(var1)

# result=lambda a,b:a+b
# print(result(6,8))
# print(result(9,8))
# squre=lambda x:x+8
# print(squre(6))
# print(squre(3))

# def addTwo(func):
#     print("Good Morning")
#     func("Rohit Kumar")
#     print("Welcome sir")

# def functionNew(name):
#     print(name)

# addTwo(functionNew)

# def square(num1):
#     return num1*num1


# numbers=[7,4,2,6]

# ListSquare=list(map(lambda x:x*x,numbers))
# print(ListSquare)

# numbers=[7,4,2,6,7,2,1,9]

# ListSquare=list(filter(lambda x:x>4,numbers))
# print(ListSquare)

# from functools import reduce
# numbers=[7,4,2,6]
# ListSquare=(reduce(lambda x,y:x+y,numbers))
# print(ListSquare)

# print(6==6)
# a=7
# b=7
# print(a==b)
# print(a is b)
a=[7,8,9]
b=[7,8,9]

print(a==b)
print(a is b)