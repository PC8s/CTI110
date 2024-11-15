# Paul Price

# 10/10/24

# P2HW2

# List of Modules

# Using lists



# Allow user to give list items
mod1 = float(input("Enter a grade: "))
mod2 = float(input("Enter a grade: "))
mod3 = float(input("Enter a grade: "))
mod4 = float(input("Enter a grade: "))
mod5 = float(input("Enter a grade: "))
mod6 = float(input("Enter a grade: "))

# Empty list
num_list = []

# Add variables to the list
num_list.append(mod1)
num_list.append(mod2)
num_list.append(mod3)
num_list.append(mod4)

# Create the list with the variables
num_list = [mod1, mod2, mod3, mod4, mod5, mod6]

# print list
print(num_list)

print("------Results------")
# Using functions with list
print(f"The lowest value is {min(num_list)} !!")
print(f"The highest value is {max(num_list)} !!")
print(f"The sum of value is {sum(num_list)} !!")
print(f"Average grade {sum(num_list)/ len(num_list)}")




