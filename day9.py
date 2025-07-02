
inputValue=int(input("Enter the numebr from 1 to 4: "))

match inputValue:
    case 11|12|13|14:
        print("Today is Sunday")
    case 25:
        print("Today is Monday")
    case 34:
        print("Today is Tuesday")
    case 4:
        print("Today is Wednesday")
    case _ if inputValue%2==0:
        print("This the even value")
    case _:
        print("This is the odd case default case")

# fruit = "apple"
# fruit = "banana"
# match fruit:
#     case "apple":
#         print("It's red or green.")
#     case "banana":
#         print("It's yellow.")
#     case _:
#         print("Unknown")