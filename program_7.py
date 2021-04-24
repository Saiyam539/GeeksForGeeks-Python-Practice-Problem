# This program wil print digit pattern
# with the help of loops in python.


def print_digit_pattern(number):
    
    for i in number:
        print('|', end='')

        print('*' * int(i))

number = input("Enter the number here:- ")
print_digit_pattern(number)
