

import sys


def isPrime(num):
    # returns error message if no argument supplied
    if not num:
        return "This function requires a single integer as input."
    num = int(num)
    # checks if num is divisible by any number greater than 1 and less than itself
    # will return false if num is divisible by any such number
    for i in range(2, num):
        if num/i % 1 == 0:
            return False
    return True


print(isPrime(sys.argv[1]))
