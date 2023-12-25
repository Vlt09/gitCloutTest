def add_numbers(a, b):
    return a + b

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_even(number):
    return number % 2 == 0
