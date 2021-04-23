# This program will print differnt patterns
# with help of loops.

# Pyramid pattern in python.

def print_pyramid():

    number = int(input('Enter the number here:- '))

    for i in range(number):
        for a in range(0, i+1):
            print('*', end='')
        print()

print_pyramid()

