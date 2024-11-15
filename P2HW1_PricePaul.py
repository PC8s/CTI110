# Paul Price
# 10/8/2024
# P2HW1
# Travel to New York


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
print("-------Travel Expenses-------")

print(f"{'Location:':<20}{state}")
print(f"{'Budget:':<20}${budget:,.2f}")
print(f"{'Fuel:':<20}${gas_price:,.2f}")
print(f"{'Accomodation:':<20}${hotel_price:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")

# leftover money
leftover=budget - gas_price - hotel_price - food

print("------------------------------\n")
print(f"Remaining Balance: ${leftover:,.2f}")

