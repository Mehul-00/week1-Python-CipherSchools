# strings
name = "harshit"
# string indexing
print(name[-1])
# string slicing
print(name[0])
print(name[0:5])
print(name[:-2])
print(name[-1:0:-1])
# take user input
age = int(input("enter your age : "))
print(age)
# take two user inputs
user_name, age = input("enter your name and age : ").split(",")
print(user_name)
print(age)

# len function
print(len(name))
# lower, upper, title method
print(name.title())
# find, replace, center method
r_pos = name.find("r")
r_pos2 = name.find("r", r_pos + 1)
print(r_pos2)
# **harshit**
print(name.center(14, "*"))
# strings are inmutable
print(name.replace("h","H",-1))
print(name)