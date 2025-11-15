import pandas as pd
import os

# --- Configuration ---
# Use the correct CSV file name
csv_file_name = "HistoricalData.csv" 
output_folder = "hw4"
output_file_name = "TSLA_log.txt"
file_path_for_txt = os.path.join(output_folder, output_file_name)

# --- 1. Create Folder and Load Data ---
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created folder: {output_folder}")

try:
    df = pd.read_csv(csv_file_name)
    
    # 2. Clean and Sort Data
    df['Close/Last'] = df['Close/Last'].replace({'\$': ''}, regex=True).astype(float)
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    df = df.sort_values(by='Date').reset_index(drop=True)

    # 3. Extract and Save ONLY the prices to TSLA.txt
    prices = df['Close/Last'].round(2).tolist()

    with open(file_path_for_txt, 'w') as f:
        for price in prices:
            # Writes one clean number per line, nothing else!
            f.write(f"{price}\n")

    print(f"✅ Data preparation complete. Cleaned prices saved to: {file_path_for_txt}")

except FileNotFoundError:
    print(f"❌ Error: Could not find the original CSV file: {csv_file_name}. Please verify the file name.")


