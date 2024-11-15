# Paul Price
# 10/24/24
# P3HW2
# Calculate reg and OT pay, given an employees hours worked

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


name = input("Enter employee name: ")

hours =float( input("Enter number of hours worked: "))

pay =float( input("Enter pay rate: "))



print("employee name", name)

# Calculate hours greater or less than 40


if hours > 40:
    OT = hours - 40
    OT_pay = pay  * 1.5
    reg = 40 * pay
    gross= OT_pay + reg
else:
    
    OT = 0
    OT_pay = 0
    reg = hours * pay
    gross= OT_pay + reg

print("total hours", hours)

print("reg payrate", pay)

print("overtime hours", OT)

print("overtime pay", hours)

print("regular hours", reg)

print("total gross", gross)


