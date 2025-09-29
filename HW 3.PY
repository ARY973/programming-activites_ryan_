# hw3.py

# Problem 3.4 Code:
for row in range(2):
    # Inner loop to print seven '@' symbols for the current row
    for symbol in range(7):
        # Print '@' without a newline, so all symbols stay on the same line
        print('@', end='')
    # Print a newline after the seven symbols to start the next row
    print()


# Problem 3.9 Code:
while True:
    # Get user input as a string and strip any whitespace
    input_str = input('Enter a number 7 to 10 digits: ').strip()

    # Validate that the input is a digit string and its length is between 7 and 10
    if input_str.isdigit() and 7 <= len(input_str) <= 10:
        break
    else:
        print('Invalid input. Please enter an integer between 7 and 10 digits.')

# Convert the valid string input to an integer
number = int(input_str)
# Get the number of digits to determine the initial divisor
num_digits = len(input_str)

# Calculate the starting divisor (10^(num_digits - 1)). E.g., for 8 digits, it's 10^7.
divisor = 10 ** (num_digits - 1)

# Loop to extract and print digits from left to right
print('\nDigits:')
# Continue the loop as long as the divisor is large enough to extract a digit
while divisor >= 1:
    # Use integer division to 'pick off' the leftmost digit
    digit = number // divisor
    # Print the extracted digit
    print(digit)

    # Use modulus to remove the extracted digit from the number for the next iteration
    number %= divisor
    # Decrease the divisor by a factor of 10 to move to the next digit position (e.g., from 10^7 to 10^6)
    divisor //= 10


# Problem 3.11 Code:
total_miles = 0.0  
total_gallons = 0.0 
count_tankfuls = 0 

# Start a sentinel-controlled loop, which will run indefinitely until the user enters the sentinel value
while True:
    try:
        # Prompt for gallons used. The sentinel is -1.0.
        gallons = float(input('\nEnter the gallons used (-1 to end): '))
    except ValueError:
        print('Invalid input. Please enter a number.')
        continue

    # Check for the sentinel value to end input and processing
    if gallons == -1.0:
        break

    # Ensure gallons is a positive value before proceeding
    if gallons <= 0:
        print('Gallons used must be a positive number.')
        continue

    try:
        # Prompt for miles driven
        miles = float(input('Enter the miles driven: '))
    except ValueError:
        print('Invalid input. Please enter a number for miles.')
        continue

    # Ensure miles is a non-negative value before proceeding
    if miles < 0:
        print('Miles driven cannot be negative.')
        continue

    # Calculate miles per gallon (MPG) for the current tankful
    mpg_tank = miles / gallons

    # Display the MPG for the current tankful, formatted to a reasonable number of decimal places
    print(f'The miles/gallon for this tank was {mpg_tank:.6f}')

    # Update accumulators for the overall average calculation
    total_gallons += gallons
    total_miles += miles
    count_tankfuls += 1

# After the loop, calculate and display the overall average
# Check if any data was entered before calculating the average (to avoid division by zero)
if count_tankfuls > 0:
    # Calculate the overall average miles per gallon
    overall_avg_mpg = total_miles / total_gallons
    # Display the overall average, formatted to a reasonable number of decimal places
    print(f'\nThe overall average miles/gallon was {overall_avg_mpg:.6f}')
else:
    print('\nNo tankfuls were entered. Exiting.')


# Problem 3.12 Code:
# Get the five-digit integer as a string
num_str = input('\nEnter a five-digit integer: ')

# Assume it's a palindrome until proven otherwise
is_palindrome = True
n = 5 # Fixed length for a five-digit number

# Loop only up to the middle of the string (for a 5-digit number, only indices 0 and 1)
# range(n // 2) is range(2) -> indices 0 and 1
for i in range(n // 2):
    # Compare the digit at index i (from the start)
    # with the digit at index n - 1 - i (from the end)
    # For i=0, compares index 0 (first) with index 4 (last)
    # For i=1, compares index 1 (second) with index 3 (second to last)
    if num_str[i] != num_str[n - 1 - i]:
        # If any pair of corresponding digits doesn't match, it's not a palindrome
        is_palindrome = False
        break # No need to check the rest of the digits

# Check the result and print the determination
if is_palindrome:
    print(f'The number {num_str} is a palindrome.')
else:
    print(f'The number {num_str} is NOT a palindrome.')



# Problem 3.14 Code:
import math

# Initialize the approximation of pi. The first term is 4/1 = 4.
pi_approx = 0.0
# Denominator starts at 1, then goes 3, 5, 7, ...
denominator = 1
# Keeps track of the term sign (starts positive)
sign = 1
# Variable to hold the previous pi approximation for the 'twice in a row' check
previous_pi_approx = 0.0

# Counters to store the iteration number when the conditions are first met
iter_314_twice = -1
iter_3141_twice = -1

# Print the table header
print('\nApproximating π:')
print('-' * 45)
print(f'| {"n":<5} | {"Denominator":<12} | {"Term":<15} | {"π Approx":<15} |')
print('-' * 45)

# Loop up to 3000 iterations as a maximum, but it can stop earlier if both conditions are met
# 'n' will represent the number of terms used, starting from 1
for n in range(1, 3001):
    # The current term is 4 / denominator, with an alternating sign.
    term = sign * (4 / denominator)

    # Add the current term to the running approximation
    pi_approx += term

    # Print the table row. The format string ensures consistent display for table alignment.
    print(f'| {n:<5} | {denominator:<12} | {term:<15.9f} | {pi_approx:<15.9f} |')

    # Logic to find the iteration count for '3.14 twice in a row'
    if iter_314_twice == -1:
        # Check if the current and previous approximations both match '3.14'
        if str(pi_approx)[:4] == '3.14' and str(previous_pi_approx)[:4] == '3.14':
            iter_314_twice = n

    # Logic to find the iteration count for '3.141 twice in a row'
    if iter_3141_twice == -1:
        # Check if the current and previous approximations both match '3.141'
        if str(pi_approx)[:5] == '3.141' and str(previous_pi_approx)[:5] == '3.141':
            iter_3141_twice = n

    # Update the previous approximation for the next iteration's check
    previous_pi_approx = pi_approx

    # Update for the next iteration:
    # 1. Flip the sign: 1 becomes -1, -1 becomes 1
    sign *= -1
    # 2. Increase the denominator by 2 to get the next odd number (1 -> 3 -> 5 -> ...)
    denominator += 2

    # Break the loop early if both required conditions have been met
    if iter_314_twice != -1 and iter_3141_twice != -1:
        break

print('-' * 45)

# Final answer print for the comment section questions
print(f'\nAnswer to the comment questions:')
print(f'Iterations required to first get 3.14 twice in a row: {iter_314_twice}')
print(f'Iterations required to first get 3.141 twice in a row: {iter_3141_twice}')

# --------------------------------------------------------------------------------