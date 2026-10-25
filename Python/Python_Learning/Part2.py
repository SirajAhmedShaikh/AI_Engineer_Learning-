#Conditonal Statements , Loops & Functions
# ex1
# age=int(input("enter a number : "))
# if age>18:
#     print("You can vote")
# else:
#     print("You can vote")

# Nesting in Conditionals
# Login System
# username = input("enter username: ")
# password = input("enter password: ")
# if (username == "admin" and password == "pass"):
#     print("log in successful!")
# else:
#     if username != "admin": # NESTING
#         print("wrong user name, try again.")
#     else:
#         print("wrong password, try again.")

# Match Case Statements
color = input("enter color: ")
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Look")
    case "green":
        print("Go")
    case _: 
        print("wrong color")




