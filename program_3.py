# This function will take input of four numbers 
# and will tell the greatest number between all four.

def find_greater_number():
    num1 = int(input("Enter the 1st number here:- "))
    num2 = int(input("Enter the 2nd number here:- "))
    num3 = int(input("Enter the 3rd number here:- "))
    num4 = int(input("Enter the 4th number here:- "))

    # First compare num1 and num2.
    if num1>num2:
        greater_number_1 = num1
    else:
        greater_number_1 = num2
    
    # Then compare num3 and num4.    
    if num3>num4:
        greater_number_2 = num3
    else:
        greater_number_2 = num4

    # Now compare greater_number_1 and greater_number_2.
    if greater_number_1>greater_number_2:
        print(f'{greater_number_1} is greater amongst all the numbers.')
    else:
        print(f'{greater_number_2} is greater amongst all the numbers')

find_greater_number()

'''The output of this code is:- 

num1 = 50
num2 = 100
num3 = 200
num4 = 10

***
200 is the greater amongst all the numbers
'''
