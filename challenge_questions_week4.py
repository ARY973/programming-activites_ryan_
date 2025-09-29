import random

def number_guessing_game():
    """
    simulates a number guessing game where the user guesses a number between 1 and 100.
    """

    #Step 1: Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    #Step 2: Initialize guess counter
    guess_count = 0

    print("welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it! You can also type 'quit' to exit.")


    while True:
        try:
            user_input = input("Enter your guess: ")

            if user_input.lower() =='quit' :
                print("Thanks for playing! The number was", secret_number)
                break
            guess = int(user_input)

            guess_count += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"congratulations! you guessed the number {secret_number} correctly.")
                print(f"It took you {guess_count} guesses.")
                break
        except ValueError:
         print("Invalid input. please enter a whole number or quit'.")

number_guessing_game()

        

        