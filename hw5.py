# File: hw5.py
# Student: Preston Cook
# UT EID: plc886
# Course: CS303E
# 
# Date: 12/16/2022
# Description of Program: Basic loop to repeatedly get user input
import math

def main():
    max, min, count = -math.inf, math.inf, 0
    
    while True:
        num = input('Enter a number: ')
        if num == 'stop':
            break
        num = int(num)
        count += 1
        max = num if num > max else max
        min = num if num < min else min
    
    if count == 0:
        print("You didn't enter any numbers")
    elif count == 1:
        print(f"You entered 1 number\nThe maximum is {max}\nThe minimum is {min}")
    else:
        print(f'You entered {count} numbers.\nThe maximum is {max}\nThe minimum is {min}')

if __name__ == '__main__':
    main()