def load_prices_from_txt(ticker):
    """
    Load prices from <ticker>.txt.

    Handles two formats:
    1) Clean:      272.95
                   273.47
    2) CSV-style:  Date,Close/Last,Volume,Open,High,Low
                   11/13/2025,$272.95,49602790,$274.11,$276.699,$272.09
    """
    filename = f"{ticker}.txt"
    prices = []

    with open(filename, "r") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue

            # Try simple numeric line first
            try:
                prices.append(float(s))
                continue
            except ValueError:
                pass  # not a plain number, try CSV parsing

            # Try CSV-style: Date,Close/Last,Volume,Open,High,Low
            parts = s.split(",")
            if len(parts) < 2:
                # can't parse, skip
                continue

            close_str = parts[1]  # "Close/Last" or like "$272.95"

            # skip header row
            if close_str == "Close/Last":
                continue

            # remove $ and any quotes/spaces
            close_str = close_str.replace("$", "").replace('"', "").strip()

            if close_str == "":
                continue

            try:
                prices.append(float(close_str))
            except ValueError:
                # bad line, skip
                continue

    return prices
import json

# ---------------------------------------------------------
# CONFIG
# ---------------------------------------------------------

STARTING_CAPITAL = 10_000.0
MA_WINDOW = 20  # moving average window (can change if your prof says so)

# 10 tickers: 3 required + 7 of your choice
tickers = [
    "AAPL",
    "GOOG",
    "ADBE",
    "TSLA",
    "BA",
    "CMCSA",
    "CSCO",
    "CVX",
    "JPM",
    "V"
]


# ---------------------------------------------------------
# HELPER: SIMPLE MOVING AVERAGE
# ---------------------------------------------------------

def simple_moving_average(prices, window):
    """
    Returns a list 'avg' of the same length as prices, where
    avg[i] is the average of the previous 'window' prices up to i.
    The first (window-1) entries are None because we don't have enough data yet.
    """
    n = len(prices)
    avg = [None] * n

    if window <= 0 or window > n:
        return avg

    # first full window
    running_sum = sum(prices[0:window])
    avg[window - 1] = running_sum / window

    # slide the window
    for i in range(window, n):
        running_sum += prices[i] - prices[i - window]
        avg[i] = running_sum / window

    return avg


# ---------------------------------------------------------
# 1) MEAN REVERSION STRATEGY
# ---------------------------------------------------------

def meanReversionStrategy(prices):
    """
    Mean reversion trading strategy.

    For each day i (once we have a moving average):
        if price < avg * 0.98:
            print("buy at: ", price)
        elif price > avg * 1.02:
            print("sell at: ", price)
        else:
            pass

    We simulate trading 1 share at a time, starting with STARTING_CAPITAL.
    At the end, we liquidate all remaining shares at the last price.

    Returns:
        profit (float), returns_pct (float)
    """
    avg = simple_moving_average(prices, MA_WINDOW)

    cash = STARTING_CAPITAL
    shares = 0

    print("----- Mean Reversion Strategy -----")

    for i, price in enumerate(prices):
        if avg[i] is None:
            continue  # skip until we have enough data for MA

        # mean reversion logic from assignment
        if price < avg[i] * 0.98:
            if cash >= price:  # buy 1 share
                cash -= price
                shares += 1
                print("buy at:", price)
        elif price > avg[i] * 1.02:
            if shares > 0:     # sell 1 share
                cash += price
                shares -= 1
                print("sell at:", price)
        else:
            # do nothing
            pass

    # liquidate remaining shares at final price
    final_price = prices[-1]
    if shares > 0:
        cash += shares * final_price
        shares = 0

    final_value = cash
    profit = final_value - STARTING_CAPITAL
    returns_pct = (profit / STARTING_CAPITAL) * 100.0

    print("Final profit:", round(profit, 2))
    print("Final return (%):", round(returns_pct, 2))
    print("-----------------------------------\n")

    return profit, returns_pct


# ---------------------------------------------------------
# 2) SIMPLE MOVING AVERAGE STRATEGY
# ---------------------------------------------------------

def simpleMovingAverageStrategy(prices):
    """
    Simple Moving Average trading strategy.

    For each day i (once we have a moving average):
        if price > avg:
            print("buy at: ", price)
        elif price < avg:
            print("sell at: ", price)
        else:
            pass

    We simulate trading 1 share at a time, same as above.

    Returns:
        profit (float), returns_pct (float)
    """
    avg = simple_moving_average(prices, MA_WINDOW)

    cash = STARTING_CAPITAL
    shares = 0

    print("----- Simple Moving Average Strategy -----")

    for i, price in enumerate(prices):
        if avg[i] is None:
            continue  # not enough data for MA yet

        # simple moving average logic from assignment
        if price > avg[i]:
            if cash >= price:  # buy 1 share
                cash -= price
                shares += 1
                print("buy at:", price)
        elif price < avg[i]:
            if shares > 0:     # sell 1 share
                cash += price
                shares -= 1
                print("sell at:", price)
        else:
            # do nothing
            pass

    # liquidate remaining shares at final price
    final_price = prices[-1]
    if shares > 0:
        cash += shares * final_price
        shares = 0

    final_value = cash
    profit = final_value - STARTING_CAPITAL
    returns_pct = (profit / STARTING_CAPITAL) * 100.0

    print("Final profit:", round(profit, 2))
    print("Final return (%):", round(returns_pct, 2))
    print("------------------------------------------\n")

    return profit, returns_pct


# ---------------------------------------------------------
# 3) SAVE RESULTS TO JSON
# ---------------------------------------------------------

def saveResults(results_dict):
    """
    Save the dictionary to a file called results.json.
    """
    with open("results.json", "w") as f:
        json.dump(results_dict, f, indent=4)
    print("Results saved to results.json")


# ---------------------------------------------------------
# 4) MAIN: LOOP OVER 10 TICKERS
# ---------------------------------------------------------

def main():
    # dictionary to store prices, profits, and return percentages
    results = {}

    for ticker in tickers:
        print(f"=== Processing {ticker} ===")

        prices = load_prices_from_txt(ticker)

        # store the prices
        results[f"{ticker}_prices"] = prices

        # run mean reversion strategy
        mr_profit, mr_returns = meanReversionStrategy(prices)
        results[f"{ticker}_mr_profit"] = mr_profit
        results[f"{ticker}_mr_returns"] = mr_returns

        # run simple moving average strategy
        sma_profit, sma_returns = simpleMovingAverageStrategy(prices)
        results[f"{ticker}_sma_profit"] = sma_profit
        results[f"{ticker}_sma_returns"] = sma_returns

    # save everything at the end
    saveResults(results)


if __name__ == "__main__":
    main()