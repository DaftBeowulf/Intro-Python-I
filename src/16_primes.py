
def isPrime(num):
    # returns error message if no argument supplied
    if not num or not isinstance(num, int) or num <= 0:
        return "This function requires a positive integer as input."
    num = int(num)
    # checks if num is divisible by any number greater than 1 and less than itself
    # will return false if num is divisible by any such number
    for i in range(2, num):
        if num/i % 1 == 0:
            return False
    return True


x = input('Enter a number to see if it\'s prime or not:')
print(isPrime(x))
