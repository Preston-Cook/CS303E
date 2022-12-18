# File: FindPrimeFactors.py
# Student: Preston Cook
# UT EID: plc886
# Course Name: CS303E
#
# Date: 12/17/2022
# Description of Program: Prime Factorization Calculator

import functools


def main():

    while True:
        num = int(input('Enter a positive integer (or 0 to stop): '))

        while num < 0 or num == 1:
            if num == 1:
                print('1 has no prime factorization.')
            else:
                print('Negative integer entered. Try again.')
            num = int(input('Enter a positive integer (or 0 to stop): '))

        if num == 0:
            print('Goodbye!')
            return 0

        print(get_prime_factors(num))


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_prime_factors(target):
    prime_factors = []
    tmp = target
    while functools.reduce(lambda x, y: x * y, prime_factors, 1) != target:
        min_prime = min(i for i in range(2, tmp + 1) if tmp % i == 0 and isPrime(i))
        prime_factors.append(min_prime)
        tmp //= min_prime
    return prime_factors


if __name__ == '__main__':
    main()