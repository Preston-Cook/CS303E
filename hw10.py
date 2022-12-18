# File: ComparingLinearBinarySearch.py
# Student: Preston Cook
# UT EID:plc886
# Course Name: CS303E
# 
# Date: 12/16/2022
# Description of Program: Comparing linear and binary search
import random as r
import math

def main():
    lst = [i for i in range(0, 1000)]
    r.shuffle(lst)

    linearSearchTests(lst)
    binarySearchTests(lst)

    return 0


def linearSearch( lst, key ):
    """ Search for key in unsorted list lst.  Note that
        the index + 1 is also the number of probes. """
    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -1

def binarySearch( lst, key ):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """
    count = 0
    low = 0
    high = len(lst) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (mid, count)
        else:
            low = mid + 1
    # Search failed
    return (-low - 1, count)

def linearSearchTests(lst):
    """Performs tests for linear search"""
    print('Linear Search: ')
    for i in range(1, 6):
        n = 10 ** i
        total_probes = 0
        for _ in range(n):
            key = r.choice(lst)
            probes = linearSearch(lst, key) + 1
            total_probes += probes
        print(f'  Tests: {n}'.ljust(18) + f'Average Probes: {total_probes / n:.5f}')

def binarySearchTests(lst):
    """Performs tests for binary search"""
    print('Binary Search: ')
    total_probes = 0
    for _ in range(1000):
        key = r.choice(lst)
        probes = binarySearch(lst, key)[-1]
        total_probes += probes
    avg_probes = total_probes / 1000
    log_calc = math.log2(1000)
    print(f'  Average number of probes: {avg_probes}')
    print(f'  log2(1000): {log_calc}')
    print(f'  Differs from log2(1000) by: {log_calc - avg_probes}')

if __name__ == '__main__':
    main()