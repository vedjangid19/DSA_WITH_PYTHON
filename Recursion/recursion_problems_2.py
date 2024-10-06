def sum_natural_number(number):
    """calculate sum of first n natural numbers."""
    if number < 0:
        return 0
    result = number + sum_natural_number(number=number-1)
    return result

def sum_odd_natural_number(number):
    """calculate sum of first n odd natural numbers."""
    if number == 1:
        return 1
    return (2 * number - 1) + sum_odd_natural_number(number - 1)

def sum_even_natural_number(number):
    """calculate sum of first n even natural numbers."""
    if number == 0:
        return 0
    return 2 * number + sum_even_natural_number(number - 1)

def factorial(number):
    """calculate factorial of n number"""
    if number == 1:
        return 1
    fact = number * factorial(number=number-1)
    return fact

def square_sum_natural_number(number):
    """ calculate sum of square of n natural numbers. """
    if number == 1:
        return 1**2
    squre_sum = number**2 + square_sum_natural_number(number=number-1)
    return squre_sum

print(f"sum of first 5 natural numbers: {sum_natural_number(5)}")
print(f"sum of first 5 odd natural numbers: {sum_odd_natural_number(5)}")
print(f"sum of first 5 even natural numbers: {sum_even_natural_number(5)}")
print(f"factorial of 5 number: {factorial(5)}")
print(f"sum of square of 5 natural numbers: {square_sum_natural_number(5)}")