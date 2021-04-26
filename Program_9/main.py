# This program will read content from file_1.txt and then will 
# print this content in the file_2.txt with the
# help of python.

def copy_content():
    with open('file_1.txt', 'r') as file_1:
        content = file_1.read()
    
    with open('file_2.txt', 'w') as file_2:
        file_2.write(content)
        print("The content has been copyed from file_1.txt\nto file_2.txt.")

copy_content()