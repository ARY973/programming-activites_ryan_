#This program calculates the user's birth year based on their age using a while loop.

from datetime import date

def calculate_birth_year():
    """
    Asks the user for their age and prints a timeline of their life,
    culminating in theirbirth year.
    """

    try:
        #Get the current year
        current_year = date.today().year

        #Get the user's age from input
        age = int(input ("please enter your current age:"))

        #make a copy of the current year to decrement in the loop
        year_to_decrement = current_year

        #Loop while the age is greater than 1 
        while age > 1:
            print(f"You were alive in year: {year_to_decrement}")
            #Decrease both the age and the year by one
            age -= 1
            year_to_decrement -= 1 
        #The 'else' block of a while loop executes when the loop condition becomes false 
        else:
            #when age becomes 1, the loop terminates and this block is executed
            print(f"you were born in year: {year_to_decrement}")

    except ValueError:
        print("Invalid input. please enter a whole number for your age.")


#Run the function
calculate_birth_year()

    
       
     
  