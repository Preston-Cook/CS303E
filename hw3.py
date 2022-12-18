# File: hw3.py
# Student: Preston Cook
# UT EID: plc886
# Course: CS303E
# 
# Date: 12/16/2022
# Description of Program: Calculates the handicaps for bowlers

def main():
    name = input("Enter a bowler's name: ")
    avg = int(sum(int(input(f'Enter game {i}: ')) for i in range(1, 4)) / 3)
    print(f'\nHandicap report for {name}:\n   {name}\'s average is: {avg}\n   {name}\'s handicap is: {calc_handicap(avg)}')
    print('\nIt\'s time to bowl!')
    return 0

def calc_handicap(avg):
    return int((200 - avg) * 0.8)

if __name__ == '__main__':
    main()