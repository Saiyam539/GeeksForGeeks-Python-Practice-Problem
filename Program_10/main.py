# This program will take input from the user 
# and then print that line.

def print_line():
    user_input = int(input('Enter the line number here:- '))
    with open('Demo_File.txt','r') as file:
        content = file.readlines()
        print(f'The line number {user_input} is:-\n{content[user_input]}')

print_line() 