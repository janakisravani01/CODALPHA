import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

portfolio = {
    'AAPL': 10,
    'MSFT': 5,
    'AMZN': 2,
    # Add more stocks as needed
}

def get_portfolio_prices(portfolio):
    prices = {}
    for symbol in portfolio.keys():
        try:
            stock = yf.Ticker(symbol)
            current_price = stock.history(period="1d").iloc[-1]['Close']
            prices[symbol] = current_price
        except:
            prices[symbol] = 'Error'
    return prices

# Get current prices for the portfolio
portfolio_prices = get_portfolio_prices(portfolio)

# Create a DataFrame for the portfolio
portfolio_df = pd.DataFrame(list(portfolio.items()), columns=['Symbol', 'Shares'])
portfolio_df['Current Price'] = portfolio_df['Symbol'].map(portfolio_prices)

# Display portfolio DataFrame
print("Current Portfolio:")
print(portfolio_df)

portfolio_df['Current Price'] = portfolio_df['Current Price'].astype(float)

plt.figure(figsize=(10, 6))
plt.bar(portfolio_df['Symbol'], portfolio_df['Current Price'] * portfolio_df['Shares'], color='blue')
plt.xlabel('Stocks')
plt.ylabel('Total Value')
plt.title('Portfolio Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
