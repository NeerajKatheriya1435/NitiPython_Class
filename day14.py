
name="Niti"
age=45

# str1="My name is {1} and age is {0}"
# print(str1.format(age,name))

# str1="My name is %s and age is %d"
# print(str1 %(name,age))

# str1=f"My name is {name} and age is {age}"
# print(str1)

# mySet={6,6,6,8,"Hello",4,2}
mySet1={6,4,5,9,3,9}
mySet2={5,3,4,6,9}
# mySet.add(999)
# print(mySet)
# mySet.remove(9)
# mySet.discard(9)
# mySet.pop()
# mySet.clear()
# newSet=mySet.copy()
# print(mySet)
# mySet.update([8,9,7,6])
# mewSetUninon=mySet1.union(mySet2)
# mewSetUninon=mySet1.intersection(mySet2)
mewSetUninon=mySet1.difference(mySet2)
# {6,4,5,9,3}-{5,3,4,6}={9}
print(mewSetUninon)