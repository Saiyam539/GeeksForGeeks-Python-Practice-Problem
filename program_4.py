# This program will print different patterns
# with the help for loops.

# Half Diamond 

def print_half_diamond():

    number = int(input('Enter the number here:- '))

    for i in range(number):
        for a in range(0, i + 1):
            print('*', end='')
        print()

    for i in range(1, number):
        for a in range(i, number):
            print('*', end='')
        print()

print_half_diamond()