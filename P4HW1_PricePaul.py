# Paul Price
# 11/5/24
# P4HW1
# Collect Items from store


# Create a list to hold valid inputs
validgrades = []

# How to grade scores in the loop
numGrade = int(input("How many scores do you need to grade?"))
for grades in range (numGrade):
    userInput = float (input(f"Enter grade # {grades + 1}: "))
    while userInput < 0 or userInput > 100:
        print("You enter a bad grade")
        userInput = float (input(f"Enter grade # {grades + 1}: "))
    validgrades.append(userInput)
print(validgrades)

print("---------Results-------")
lowest_grade = min(validgrades)
print(f"lowest scores: {lowest_grade}")
validgrades.remove(lowest_grade)
print(f"Modified List: {validgrades}")


print("--------------------")
avg = sum(validgrades)/ len(validgrades)
# Branching to determine the letter grade
letter_grade = ""

if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else: # letter_grade less than 60
    letter_grade = "F"
print(f"average scores: {avg}")
print()
print(f"Your grade is: {letter_grade}")



