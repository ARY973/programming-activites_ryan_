import os

# --- Configuration (Using the robust path setup) ---
data_file_path = os.path.join("hw4", "TSLA.txt") 
log_file_path = os.path.join("hw4", "TSLA_LOG_10DAY.txt") # New log file to distinguish the test

# --- 1. Data Loading ---
prices = []
try:
    with open(data_file_path, "r") as file:
        lines = file.readlines()
        
    for line in lines:
        try:
            price = round(float(line.strip()), 2)
            prices.append(price)
        except ValueError:
            continue
except FileNotFoundError:
    print(f"FATAL ERROR: The data file '{data_file_path}' was not found. Please verify the hw4 folder and file name.")
    exit()

# Note: We need 11 days now (10 for MA + 1 for current day)
window_size = 10 
if len(prices) < window_size + 1: 
    print(f"❌ Error: Not enough data read ({len(prices)} prices). Need at least {window_size + 1} days for this strategy.")
    exit()

# --- 2. Trading Logic Initialization (NEW MEAN REVERSION) ---
buy_price = None          
first_buy = None          
total_profit = 0.0        
has_stock = False         

# --- 3. Main Trading Loop ---
# Open the log file for writing (this will overwrite previous runs)
with open(log_file_path, 'w') as log_file:
    
    log_file.write("--- Individual Trade Profits (10-Day MA, 1% Threshold) ---\n")
    print("\n--- Individual Trade Profits (10-Day MA, 1% Threshold) ---")

    # Loop starts from index 10 to ensure 10 preceding days exist
    for i in range(window_size, len(prices)): 
        current_price = prices[i] 
        previous_days = prices[i - window_size : i]
        avg_price = sum(previous_days) / window_size
        
        # IF: BUY Condition (1% below 10-day MA: 0.99)
        if current_price < avg_price * 0.99: 
            if not has_stock:
                buy_price = current_price
                has_stock = True
                if first_buy is None:
                    first_buy = current_price
                
                log_line = f"Day {i+1}: 🟢 BUY at ${buy_price:.2f}\n"
                log_file.write(log_line)
                print(log_line.strip())
                
        # ELIF: SELL Condition (1% above 10-day MA: 1.01)
        elif current_price > avg_price * 1.01: 
            if has_stock:
                sell_price = current_price
                trade_profit = sell_price - buy_price
                total_profit += trade_profit
                
                log_line = f"Trade {i+1}: Profit = ${trade_profit:.2f} (Sell: ${sell_price:.2f}, Buy: ${buy_price:.2f})\n"
                log_file.write(log_line)
                print(log_line.strip())
                
                buy_price = None
                has_stock = False

        # ELSE: HOLD
        else:
            pass 

    # --- 4. Final Calculations and Output ---
    final_output = "\n" + "="*40 + "\n"
    final_output += "📈 Final Trading Results (Mean Reversion: 10-Day MA, 1% Bands)\n"
    final_output += "="*40 + "\n"
    
    if first_buy is not None:
        final_profit_percentage = (total_profit / first_buy) * 100 if first_buy != 0 else 0.0
        
        final_output += f"First Buy Price: ${first_buy:.2f}\n"
        final_output += f"Total Profit from all trades: ${total_profit:.2f}\n"
        final_output += f"Final Profit Percentage: {final_profit_percentage:.2f}%\n"
    else:
        final_output += "No buy trades were executed based on the strategy.\n"

    # Write final results to the log file and print to the terminal
    log_file.write(final_output)
    print(final_output)

print(f"\n✅ All trade logs and final results saved to: {log_file_path}")