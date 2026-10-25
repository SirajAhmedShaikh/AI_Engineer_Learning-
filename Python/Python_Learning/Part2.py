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
# color = input("enter color: ")
# match color:
#     case "red":
#         print("Stop")
#     case "yellow":
#         print("Look")
#     case "green":
#         print("Go")
#     case _: 
#         print("wrong color")

# Loops
# A loop lets us execute a block of code multiple times

# The while Loops
# Example 1 - print 1 to 5
# i = 1
# while i <= 5:
#     print(i) #Ifinite loop
# i += 1

# # Example 2 - print 5 to 1
# i = 5
# while i > 0:
#     print(i)  #Ifinite loop
# i -= 1


# while True: # DO NOT RUN this code
# print("Prime")

# The Contiue keyword
# It skips the rest of the current iteration and moves to the next one

# Skip multiples of 3
# i = 0
# while(i < 10):
#     i += 1
#     if(i % 3 == 0):
#         continue;
#     print(i)
 # output: 1, 2, 4, 5, 7, 8, 10


# The break keyword
# It stops the loop immediately.

# Break for multiple of 6
# i = 1
# while i <= 10:
#     if(i % 6 == 0):
#         break
#     print(i)
#     i += 1
# output: 1, 2, 3, 4, 5

# The for Loops
# Let’s look at an example:
for i in range(5):
    print(i)
# output: 0, 1, 2, 3, 4 

# single argument - start
for i in range(5):
    print(i)
# output: 0, 1, 2, 3, 4
# 2 arguments - start, stop
for i in range(1, 6):
    print(i)
# output: 1, 2, 3, 4 , 5
# 3 arguments - start, stop, step
for i in range(1, 10, 2):
    print(i)
# output: 1, 3, 5, 7, 9