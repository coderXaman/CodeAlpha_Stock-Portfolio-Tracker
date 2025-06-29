# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 125,
    "MSFT": 300
}

# Dictionary to store user's portfolio
portfolio = {}

# User input for stocks
print("Enter your stock portfolio (type 'done' to finish):")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Please try again.\n")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.\n")

# Calculate total investment
total_investment = 0
print("\nYour Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save result to file
save = input("\nWould you like to save this summary to a text file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock}: {quantity} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")
    print("Portfolio saved to 'portfolio_summary.txt'")
