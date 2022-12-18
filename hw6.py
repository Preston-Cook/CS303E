# File: hw6.py
# Student: Preston Cook
# UT EID: plc886
# Course: CS303E
# 
# Date: 12/16/2022
# Description of Program: Basic loop to repeatedly get user input
import math

# Function 1
def sumThreeNumbers (x, y, z):
    return x + y + z

# Function 2
def multiply3Numbers(x=0, y=0, z=0):
    return x * y * z

# Function 3
def sumUpTo3Numbers (x, y=0, z=0):
    return x + y + z

# Function 4
def multiplyUpTo3Numbers (x, y=1, z=1):
    return x * y * z

# Function 5
def printInOrder(x, y):
    if x < y:
        print(x, y)
    else:
        print(y, x)

# Function 6
def areaOfSquare(side):
    if side < 0:
        raise ValueError
    return side ** 2

# Function 7
def perimeterOfSquare(side):
    if side < 0:
        raise ValueError
    return side * 4

# Function 8
def areaOfCircle(radius):
    if radius < 0:
        raise ValueError
    return math.pi * radius ** 2

# Function 9
def circumferenceOfCircle(radius):
    if radius < 0:
        raise ValueError
    return math.pi * radius * 2

# Function 10
def bothFactors(d1, d2, x):
    return x % d1 == 0 and x % d2 == 0

# Function 11
def squareAndCircle(x):
    print(areaOfCircle(x))
    print(circumferenceOfCircle(x))
    print(areaOfSquare(x))
    print(perimeterOfSquare(x))

# Function 12
def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod