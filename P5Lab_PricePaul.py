# Paul Price
# 11/14/24
# P5 Lab
# Use functions to simulate self-checkout

'''
# Regular Division
print(100/3)

# Floor Division
print(100//3)

# Modules Division
print(100%3)
print(7%4)
'''

import random

def calcCashBack():
    # Generate a random float for amount owed to store
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed:.2f}")
    cash = float(input("How much cash will you put in self-checkout?"))
    # Calculate cash back
    cash_back = cash - total_owed
    return cash_back



def disperseCashBack(money):
    
    # Considering if the user put in 0.00
    if money == 0:
        print("No change")

    if money < 0:
        print("OUCH! you're in debt")

    # Check for debt
    if money > 0:
        

        # Convert money to a whole number
        money =int(round(money * 100, 2))

        #print(money)


        # Calculate the amount of dollar in the money variable
        num_dollars = money // 100
        #print(f"Dollars: {num_dollars}")

        # Remove the dollars from money variable
        money = money - (num_dollars * 100)

        # Calculate the amount of quarters in the money variable
        num_quarters = money // 25
        #print(f"Quarters: {num_quarters}")

        # Remove the quarters from money variable
        money = money - (num_quarters * 25)

        # Calculate the amount of quarters in the money variable
        num_dimes = money // 10
        #print(f"dimes: {num_dimes}")

        # Remove the quarters from money variable
        money = money - (num_dimes * 10)



        # Calculate the amount of quarters in the money variable
        num_nickels = money // 5
        #print(f"nickels: {num_nickels}")

        # Remove the quarters from money variable
        money = money - (num_nickels * 5)

        # Create a variable for pennies
        num_pennies = money
        #print(f"pennies: {num_pennies}")

    else:
        num_dollars = 0
        num_quarters = 0
        num_dimes = 0
        num_nickels = 0
        num_pennies = 0

    # print dollar amount gramatically correct
    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} dollar")
        else: # variable is greater than one
            print(f"{num_dollars} dollars")


    # print quarters amount gramatically correct
    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} quarter")
        else: # variable is greater than one
            print(f"{num_quarters} quarters")


    # print dimes amount gramatically correct
    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} dime")
        else: # variable is greater than one
            print(f"{num_dimes} dimes")      


    # print nickels amount gramatically correct
    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} nickel")
        else: # variable is greater than one
            print(f"{num_nickels} nickels")      
        

    # print pennies amount gramatically correct
    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} pennie")
        else: # variable is greater than one
            print(f"{num_pennies} pennies")
    

# Define the main
def main():
    print("Welcome to the self-checkout")
    cash_back = calcCashBack()
    print(f"Change is ${cash_back:.2f}")
    disperseCashBack(cash_back)


# Call the main
if __name__ == "__main__":
    main()
