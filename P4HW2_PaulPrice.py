# Paul Price

# 11/7/24

# P4HW2




'''
Input: Get the name as a string
Input: Get the hours worked as an Integer
Input: Get the pay rate as a float

Output: Print employee name

If hours worked is greater than 40:
    Calculate OT hours worked by subtracting 40 from hours worked
    Calculate OT pay (OT hours * (pay rate * 1.5))
    Calculate reg pay (40 * regular pay rate)
    Calculate gross by adding OT pay and reg pay


else (employee worked 40 ore less hours):
    overtime hours = 0
    overtime pay = 0
    calculate reg pay by multiplying oringinal hours work by reg pay
    Calculate gross pay is equal to regular pay




Output:
Display total hours worked
Display regular pay rate
Display overtime hours worked
Display OT pay (OT hours times OT pay rate)
Display pay for regular hours worked at reg pay rate
Display gross pay - both reg pay and OT pay
'''

# Input employee hours


name = input("Enter employee name or done: ")
total = 0
total_OT = 0
total_RH = 0
total_gross = 0
while name.lower() != "done":
    total += 1
    hours =float( input("Enter number of hours worked: "))

    pay =float( input("Enter pay rate: "))



    print("employee name", name)

    # Calculate hours greater or less than 40


    if hours > 40:
        OT = hours - 40
        OT_pay = pay  * 1.5 * OT
        reg = 40 * pay
        gross= OT_pay + reg
        total_OT += OT_pay
        total_RH += reg
        total_gross += gross
    else:
        
        OT = 0
        OT_pay = 0
        reg = hours * pay
        gross= OT_pay + reg
        total_OT += OT_pay
        total_RH += reg
        total_gross += gross
    
    print("total hours", hours)

    print("reg payrate", pay)

    print("overtime hours", OT)

    print("overtime pay", OT_pay)

    print("regular hours", reg)

    print("total gross", gross)

    name = input("Enter employee name or done: ")
print(f"number of employees entered {total}")
print(f"total amount paid for overtime ${total_OT:.2f}")
print(f"total amount paid for regular ${total_RH:.2f}")
print(f"total amount paid for gross ${total_gross:.2f}")


