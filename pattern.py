""""

input =5
*
**
***
****
*****

input=5


*****
****
***
**
*

    *
   **
  ***
 ****
*****


   *
  ***
 *****
*******

   *
  ***
 *****
*******
 *****
  ***
   *





input=5


    *
   **
  ***
 ****
*****

"""
# n=10
# for i in range(1,n):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("\n")


# num=5
# while(num>0):
#     last=num
#     num=num-1
#     while(last>0):
#         print("*",end=" ")
#         last=last-1
#     print("\n")

n=6
m=1
for i in range(1,n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for k in range(1,m+1):
        # print(k)
        print("*",end=" ")
    m=m+2
    print("\n")