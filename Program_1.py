# This programme will detect if a string input
# is a binary or not 

def string_detection():

    main_string = input('Enter a string here:- ')

    s = ('0', '1')

    if main_string==s or main_string=='1' or main_string=='0':
        print(f"Yes {main_string} is a binary.")
    
    elif '1' in main_string or '0' in main_string:
        print(f"Yes '{main_string}' is a binary.")
    
    else:
        print(f'No "{main_string}" is not a binary.')


string_detection()

'''
The output of this code is:- 
***
case 1
main_string = 101010101
yes '101010101' is a binary
***

case 2
main_string = Hello
No "Hello" is not a binary
'''
