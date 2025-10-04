# Create the list and assign the values.
colors = ["blue", "green", "purple"]

# For loop through the values in the list.
print("Activity 1 Output:")
for color in colors:
    print(color)


#Activity 2
# Assuming 'colors' list from Activity 1 is available
colors = ["blue", "green", "purple"]

print("\nActivity 2 Output:")
# Outer loop to iterate through the colors in the list
for color in colors:
    print(f"Characters in '{color}':")
    # Nested for loop, to iterate through the characters in each color.
    for char in color:
        print(f"  {char}")

#Activity 3
import random

# Create an empty list.
random_numbers = []

# For loop 10 times and append a random number each time.
# Generating random integers between 1 and 100 for variety
for _ in range(10):
    number = random.randint(1, 100)
    random_numbers.append(number)

print("\nActivity 3 Output:")
print("Generated List:", random_numbers)

#Activity 4
# Assuming 'random_numbers' list from Activity 3 is available
# Example list for demonstration (will use the one generated above if run sequentially)
# random_numbers = [10, 5, 2, 4, 1, 8, 12, 3, 6, 9] 
# (Using the list generated in Activity 3 for the actual code run)

print("\nActivity 4 Output:")
print("Checking List:", random_numbers)
list_length = len(random_numbers)

# Loop through the list up to the second-to-last element
# to safely check lst[count] and lst[count+1]
for i in range(list_length - 1):
    current_number = random_numbers[i]
    next_number = random_numbers[i + 1]

    # Check if the current number and next number are both even (remainder is 0 when divided by 2)
    if current_number % 2 == 0 and next_number % 2 == 0:
        print(f"Two even numbers in a row found: {current_number} and {next_number} (at indices {i} and {i+1})")

#Activity 5
# Programming Activity 5 Solution

# 1. Read data from the file and convert to a list of floats
file = open("/home/ubuntu/environment/AAPL.txt")
lines = file.readlines()
# Use a list comprehension for a very short conversion loop
prices = [float(line) for line in lines]

# 2. Calculate average for the entire dataset
total_avg = sum(prices) / len(prices)
print("Total Average:", f"${total_avg:.2f}")

# 3. Calculate average for the first 5 days
# Use slicing (prices[:5]) and sum() for conciseness
five_day_avg = sum(prices[:5]) / 5
print("Five Day Average:", f"${five_day_avg:.2f}")

#Activity 5.2
# Programming Activity 5.2 Solution (Cleanest Version)

# --- Reading Data from File ---
file = open("/home/ubuntu/environment/AAPL.txt")
lines = file.readlines()
# Create the list of floats using a concise list comprehension
prices = [float(line) for line in lines]

# --- Moving Average and Strategy Variables ---
N = 4
total_days = len(prices)
shares = 0
cash = 0.0

# --- Required Averages (Activity 5.2, Steps 2 & 3) ---
avg_first_4 = sum(prices[:N]) / N
avg_last_4 = sum(prices[-N:]) / N

# --- Calculate All Moving Averages (Activity 5.2, Step 4) ---
# Calculates the N-day average for every day starting from the Nth day.
moving_averages = [
    sum(prices[i - N + 1:i + 1]) / N
    for i in range(N - 1, total_days)
]

# --- Trading Strategy (Activity 5.2, Steps 5 & 6) ---
# Initial BUY on the first day the MA is calculated (Day N, Index N-1)
initial_price = prices[N-1]
shares = 10
initial_investment = initial_price * shares
cash -= initial_investment

# Iterate through the rest of the days to apply the strategy
for i in range(N, total_days):
    current_price = prices[i]
    current_ma = moving_averages[i - N] # MA corresponding to the current day

    # SELL Signal: Price drops 2% below MA
    if shares > 0 and current_price < current_ma * 0.98:
        cash += current_price * shares
        shares = 0
    # BUY Signal: Not holding shares AND price rises 2% above MA
    elif shares == 0 and current_price > current_ma * 1.02:
        cash -= current_price * 10
        shares = 10

# --- Display Profit (Activity 5.2, Step 7) ---
final_portfolio_value = cash + (shares * prices[-1])
strategy_profit = final_portfolio_value - initial_investment

print("\n--- Programming Activity 5.2 Results ---")
print(f"Average of the first {N} days: ${avg_first_4:.2f}")
print(f"Average of the last {N} days: ${avg_last_4:.2f}")
print(f"Initial Investment: ${initial_investment:.2f}")
print(f"Strategy Profit: **${strategy_profit:.2f}**")

