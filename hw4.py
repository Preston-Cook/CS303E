# File: hw4.py
# Student: Preston Cook
# UT EID: plc886
# Course: CS303E
# 
# Date: 12/16/2022
# Description of Program: Basic Decision Tree to decide if customer will purchase computer

def main():
    age = int(input("Please enter person's age: "))
    income = input("Person's income (High, Medium, Low): ")
    isStudent = input("Is this person a student (Yes or No)?: ") == 'Yes'
    hasGoodCredit = input("Does this person have good credit (Yes or No)?: ") == 'Yes'

    if age > 40 and hasGoodCredit and income in ['Low', 'Medium']:
        print('This person will not purchase a computer.')
    elif not isStudent and age <= 30 and income in ['High', 'Medium']:
        print('This person will not purchase a computer.')
    else:
        print('This person will purchase a computer.')
    return 0

if __name__ == '__main__':
    main()