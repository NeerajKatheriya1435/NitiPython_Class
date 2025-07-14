# x=10
# # X=78
# x=67 #update
# print(x)
# print(X)

# def showDetails():
#     global x
#     x=56
#     print("Helllo Niti",x)

# showDetails()
# print(x)

# niti=open("./data.txt","r")
# content=niti.read()
# print(content)

# f=open("manik.txt","w")
# f=open("manik.txt","rt")
# f.write("\nHello Gyus Kaise ho1234")

# cont=f.read()
# f.close()
# print(cont)

with open("manik.txt","r+") as f:
    cont=f.read()
    f.close()
    print(cont)
