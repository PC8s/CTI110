# Paul Price
# 9/17/2024
# P1HW1
# Input and Output with mathematical expressions

print("---Calulating Exponenets---")
print ()
print ()

# Get base value (as an integar) from the user
base_value = int(input("Enter an integer as a base value: "))

# Get exponent value from user
power = int(input("Enter an integer as an exponent: "))

# Raise the base_value to the exponent
answer = base_value ** power

print ()
print ()

# Display output to the user
print(base_value, "raised to the power of", power, "is", answer, "!!")

print(answer)

print()
print()
print("--Addition and Subtraction--")
print()
print()
start_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
sub_num = int(input("Enter an integer to subtract: "))
print ()
print ()
print (start_num, "+", add_num, "-", sub_num, "is equal to", start_num + add_num - sub_num)
