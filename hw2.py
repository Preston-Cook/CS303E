# File: hw2.py
# Student: Preston Cook
# UT EID: plc886
# Course: CS303E
# 
# Date: 12/16/2022
# Description of Program: Returns the date of Easter Sunday given a year

'''Ask the user for the year (such as 2001). Save the year in variable y. See below for how to do this.
Divide y by 19 and call the remainder a. Ignore the quotient.
Divide y by 100 to get a quotient b and a remainder c.
Divide b by 4 to get a quotient d and a remainder e.
Divide (8 * b + 13) by 25 to get a quotient g. Ignore the remainder.
Divide (19 * a + b - d - g + 15) by 30 to get a remainder h. Ignore the quotient.
Divide c by 4 to get a quotient j and a remainder k.
Divide (a + 11 * h) by 319 to get a quotient m. Ignore the remainder.
Divide (2 * e + 2 * j - k - h + m + 32) by 7 to get a remainder r. Ignore the quotient.
Divide (h - m + r + 90) by 25 to get a quotient n. Ignore the remainder.
Divide (h - m + r + n + 19) by 32 to get a remainder p. Ignore the quotient.'''

def main():
    y = int(input('Enter a year: '))
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e =  b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    print(f'In {y} Easter Sunday is on month {n} and day {p}')
    return 0

if __name__ == '__main__':
    main()