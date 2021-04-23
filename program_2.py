# This program will take three diferent inputs from the user and make a list
# of all three inputs and then replace last and first element of the list.

def exchange_elements():
    input_1 = input("Enter the first element here:- ")
    input_2 = input('Enter the second element here:- ')
    input_3 = input("Enter the third element here:- ")

    list_1 = [input_1, input_2, input_3]
    print(f'This is the real string- {list_1}')
    elements = list_1[0] , list_1[2]

    list_1[2] , list_1[0] = elements

    print(f'This is the second list- {list_1}')

exchange_elements()

'''
The output of this code is 
if the string is [12,23,45]
***
This is the real string- [12,23,45] 
This is the second string- [45,23,45]
***
'''

