# Paul Price

# 10/29/24

# P4LAB1

# Use loops and turtle library to draw a house

# Import turtle library
import turtle

# Set up the window and turtle object
window = turtle.Screen()
mike = turtle.Turtle()

# Change features of turtle
mike.pensize(10)
mike.pencolor("green")
mike.shape("arrow")

# While loop that runs 4 times
movement = 0

while movement <= 3:
    movement += 1
    mike.forward(150)
    mike.right(90)

# For loop to run 3 times
for side in range(3):
    mike.forward(150)
    mike.left(120)
