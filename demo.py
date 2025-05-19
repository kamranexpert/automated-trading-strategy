from ib_insync import *

# Connect to TWS or IB Gateway (must be running and API enabled)
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

# Define the stock contract
contract = Stock('AAPL', 'SMART', 'USD')

# Request live market data (optional)
market_data = ib.reqMktData(contract, '', False, False)
ib.sleep(2)  # wait a moment for data to populate

print(f"AAPL Bid: {market_data.bid}, Ask: {market_data.ask}")

# Place a simple market order (BUY 1 share)
order = MarketOrder('BUY', 1)
trade = ib.placeOrder(contract, order)

# Wait for the order to process
ib.sleep(3)
print("Order status:", trade.orderStatus.status)

# Disconnect from IB
ib.disconnect()
