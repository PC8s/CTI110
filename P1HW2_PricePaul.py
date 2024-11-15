# Paul Price
# 9/26/2024
# P1HW2
# Travel to Alanta Georgia


print("This program calculates and display travel expenses")


# Get budget info from user
budget= float(input("Enter Budget: "))

# Get travel info from user
state= input("Enter destionation: ")

# Get gas info from user
gas_price=float(input("Enter gas price: "))

# price on hotel
hotel_price=float(input("Enter hotel price: "))

#need food for travel
food= float(input("Enter money for food: "))

print()
print("--Travel Expenses--")

print("location: ",state)
print("budget: " ,budget)

print()
print("fuel: " ,gas_price)
print("accomodation: " ,hotel_price)
print("food: " ,food)

# leftover money
leftover=budget - gas_price - hotel_price - food

print("balance: " ,leftover)
