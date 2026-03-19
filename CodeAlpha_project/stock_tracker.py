# 1. Hardcoded Stock Prices (The "Market")
market_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 370,
    "AMZN": 145
}

def run_stock_tracker():
    print("--- Personal Stock Tracker ---")
    portfolio = {}
    total_value = 0

    # 2. User Input Loop
    while True:
        symbol = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        if symbol == 'DONE':
            break
        
        if symbol in market_prices:
            try:
                shares = int(input(f"How many shares of {symbol} do you own? "))
                portfolio[symbol] = shares
            except ValueError:
                print("Invalid input. Please enter a whole number for shares.")
        else:
            print(f"Sorry, {symbol} is not in our price database.")

    # 3. Calculation and Display
    print("\n--- Portfolio Summary ---")
    summary_lines = ["Stock | Shares | Price | Subtotal\n", "-" * 35 + "\n"]
    
    for symbol, shares in portfolio.items():
        price = market_prices[symbol]
        subtotal = shares * price
        total_value += subtotal
        
        line = f"{symbol}: {shares} shares @ ${price} = ${subtotal}"
        print(line)
        summary_lines.append(line + "\n")

    print(f"\nTotal Investment Value: ${total_value}")
    summary_lines.append(f"\nTotal Investment Value: ${total_value}")

    # 4. File Handling (Save to .txt)
    save_choice = input("\nWould you like to save this report to 'portfolio.txt'? (y/n): ").lower()
    if save_choice == 'y':
        with open("portfolio.txt", "w") as file:
            file.writelines(summary_lines)
        print("Report saved successfully!")

if __name__ == "__main__":
    run_stock_tracker()