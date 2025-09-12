# Programming Activity 1

# 1. variable for apple price
apple_price = 2.5   # dollars per apple

# 2. variable for number purchased
number_purchased = 4

# 3. tax variable
tax = 1.07

# 4. calculate total bill
total_bill = apple_price * number_purchased * tax

# 6. check before printing
if total_bill == 0:
    print("Error: Please check your inputs, total bill cannot be $0.")
else:
    # 5. print clearly
    print(f"You purchased {number_purchased} apples.")
    print(f"Your total bill is: ${total_bill:.2f}")




