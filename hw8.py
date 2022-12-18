# File: hw8.py
# Student: Preston Cook
# UT EID: plc886
# Course: CS303E
# 
# Date: 12/16/2022
# Description of Program: String Method Functions
def myAppend( s, ch ):
    # Return a new string that is like s but with 
    # character ch added at the end
    return s + ch

def myCount( s, ch ):
    count = 0
    # Return the number of times character ch appears
    # in s.
    for char in s:
        if char == ch:
            count += 1
    
    return count

def myExtend( s1, s2 ):
    # Return a new string that contains the elements of
    # s1 followed by the elements of s2, in the same
    # order they appear in s2.
    return s1 + s2

def myMin( s ):
    # Return the character in s with the lowest ASCII code.
    # If s is empty, print "Empty string: no min value"
    # and return None.
    if not s:
        print('Empty string: no min value')
        return None

    min_char = s[0]
    for i in range(1, len(s)):
        if ord(s[i]) < ord(min_char):
            min_char = s[i]
    return min_char


def myInsert( s, i, ch ):
    # Return a new string like s except that ch has been
    # inserted at the ith position. I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of s and return None.
    if i > len(s):
        print('Invalid Index')
        return None
    
    s1 = ''
    for index in range(len(s)):
        if index == i:
            s1 += ch
        s1 += s[index]
    return s1

def myPop( s, i ):
    # Return two results: 
    # 1. a new string that is like s but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(s), and return s unchanged and None
    if i >= len(s):
        print('Invalid Index')
        return None
    
    s1 = ''
    for index in range(len(s)):
        if index == i:
            char = s[index]
        else:
            s1 += s[index]
    return s1, char

def myFind( s, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    for i in range(len(s)):
        if s[i] == ch:
            return i 
    return -1

def myRFind( s, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    for i in range(len(s)-1, -1, -1):
        if s[i] == ch:
            return i 
    return -1
    

def myRemove( s, ch ):
    # Return a new string with the first occurrence of ch 
    # removed. If there is none, return s.
    flag = False

    s1 = ''
    for char in s:
        if char == ch and not flag:
            flag = True
        else:
            s1 += char
    
    return s1


def myRemoveAll( s, ch ):
    # Return a new string with all occurrences of ch.
    # removed. If there are none, return s.
    s1 = ''
    for char in s:
        if char != ch:
            s1 += char
    
    return s1

def myReverse( s ):
    # Return a new string like s but with the characters
    # in the reverse order.
    s1 = ''
    for i in range(len(s) - 1, -1, -1):
        s1 += s[i]

    return s1