def print_natural_number(number):
    if number == 0:
        return
    print_natural_number(number=number-1)
    print(number, end='  ')

def print_natural_number_reverse(number):
    """Print First n Natural numbers in reverse order."""
    if number == 0:
        return
    
    print(number, end='  ')
    print_natural_number_reverse(number=number-1)

def print_odd_natural_number(number):
    """ print first n odd natural Numbers. """
    if number > 0:
        print_odd_natural_number(number=number-1)
        print(2 * number - 1, end='  ')

def print_even_natural_number(number):
    """ print first n odd natural Numbers. """
    if number > 0:
        print_even_natural_number(number=number-1)
        print(2 * number, end='  ')

def print_odd_natural_number_reverse(number):
    """ print first n odd natural Numbers. """
    if number == 0:
        return
    
    print(2 * number - 1, end='  ')
    print_odd_natural_number_reverse(number=number-1)

def print_even_natural_number_reverse(number):
    """ print first n odd natural Numbers. """
    if number == 0:
        return

    print(2 * number, end='  ')
    print_even_natural_number_reverse(number=number-1)

print_natural_number(number=3)
print()
print_natural_number_reverse(number=3)
print()
print_odd_natural_number(number=5)
print()
print_even_natural_number(number=5)
print()
print_odd_natural_number_reverse(number=6)
print()
print_even_natural_number_reverse(number=6)