# This program will make a flashcards for cars
# with the help of classes in python.

class flashcard:

    def __init__(self,name_of_car, company):
        self.name_of_car = name
        self.price = company

    def print_flashcard():
        name_of_car = input('Enter the name of car here:- ')       
        company_of_car = input('Enter the company of the car here:- ')

        flashcard = f"Name of car- {name_of_car}\nCompany of car- {company_of_car}"
        print(flashcard)

        user_choice = input("Press 'A' to continue and press 'Q' to quit:- ")

        if user_choice=='a':
            return True
        elif user_choice=='q':
            return False
            print("Thanks for using this program.")
            exit()
        else:
            print("Please enter a valid input.")

while True:
    flashcard.print_flashcard()
