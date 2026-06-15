import csv

market_rates = {
    "RELIANCE": 2950,
    "TCS": 4150,
    "INFY": 1620,
    "HDFCBANK": 1580,
    "TATAMOTORS": 980
}

user_portfolio = {}
grand_total = 0

print("=== Indian Stock Portfolio Tracker ===")

while True:
    ticker = input("\nEnter NSE Stock Symbol (e.g., TCS, RELIANCE) or 'done' to finish: ").upper().strip()

    if ticker == "DONE":
        break

    if ticker not in market_rates:
        print("Error: That symbol is not in our system. Try TCS, RELIANCE, INFY, HDFCBANK, or TATAMOTORS.")
        continue

    try:
        shares_bought = int(input(f"Enter number of shares you own for {ticker}: "))
        if shares_bought <= 0:
            print("Please enter a number greater than 0.")
            continue
    except ValueError:
        print("Invalid input. Please enter a whole number for the quantity of shares.")
        continue

    user_portfolio[ticker] = user_portfolio.get(ticker, 0) + shares_bought

print("\n" + "="*45)
print(f"{'Stock Symbol':<14} | {'Shares':<8} | {'Price (₹)':<10} | {'Total Value (₹)':<12}")
print("-"*45)

with open("portfolio.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock Symbol", "Shares Owned", "Current Market Price (INR)", "Total Holdings Value (INR)"])

    for ticker, shares_bought in user_portfolio.items():
        share_price = market_rates[ticker]
        holdings_value = share_price * shares_bought
        grand_total += holdings_value

        print(f"{ticker:<14} | {shares_bought:<8} | ₹{share_price:<9} | ₹{holdings_value:<12}")
        writer.writerow([ticker, shares_bought, share_price, holdings_value])

    writer.writerow([])
    writer.writerow(["Grand Portfolio Value", "", "", f"INR {grand_total}"])

print("-"*45)
print(f"Grand Portfolio Value: ₹{grand_total}")
print("="*45)

print("\nSuccess: Your holdings have been saved to 'portfolio.csv'!")
