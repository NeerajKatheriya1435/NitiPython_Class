import time

# time1=time.localtime()
# time1=time.time()
# print(time1)
# for i in range(100000):
#     print(i)
# time2=time.time()-time1
# print(time2)
# a=True
# print(a:=False)

def count_up_to(n):
    for i in range(n):
        yield i

gen = count_up_to(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# request module, time module, generators, walrus operators



