#programming activities 1 
#Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years:

def get_generation():
    """
    Asks the user for their birth year and prints their corresponding generation.
    """
    try:
        #prompt the user to enter their birth year and convert it into an integer
        birth_year = int(input("please enter the year you were born: "))

        #check the birth year against the specified ranges to determine the generation
        if birth_year >= 1997:
            print(f"Based on your birth year of {birth_year}, you are a memeber of Generation Z (Zoomer).")
        elif birth_year >= 1981:
            print(f"Based on your birth year of {birth_year}, you are a millenial.")
        elif birth_year >=1965:
            print(f"Based on your birth year of {birth_year},you are a member of generation x.")
        elif birth_year >=1946:
            print(f"Based on your birth year of {birth_year}, you are a baby boomer.")
        else:
            print(f"Based on your birth year of {birth_year}, you were born before the Baby Boomer Generation.")


    except ValueError:
        #Handle cases where the user enters a non-integer value
        print("Invalid input. Please enter a valid year using digits (eg., 1990).")

#Call the function to run the program
get_generation() 
   
    

        