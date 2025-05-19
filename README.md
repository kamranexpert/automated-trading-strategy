# Automated Trading Strategy

This repository contains a simple automated trading bot that connects to Interactive Brokers (IBKR) using the `ib_insync` Python library. It demonstrates how to establish a connection with TWS or IB Gateway, fetch real-time market data, and execute a basic market order.

---

## 🚀 Features

- Connects to IBKR Trader Workstation (TWS) or IB Gateway
- Requests live market data for any supported asset (e.g., stocks)
- Places a basic market buy order
- Prints bid/ask prices and order status to the console

---

## ⚙️ Requirements

- Python 3.7 or higher
- IBKR account (Paper or Live)
- IB Gateway or Trader Workstation (must be running)
- API access enabled in IBKR software
- `ib_insync` library (install via pip)

---

## 🧪 Usage

1. **Start TWS or IB Gateway**  
   - Log in to your IBKR paper or live account  
   - Go to `Configure > API > Settings`  
   - Enable:
     - "Enable ActiveX and Socket Clients"
     - Optional: "Read-Only API"  
   - Use port `7497` for paper trading (default)

2. **Install Python dependencies**  
   Use `pip install ib_insync` to install the required library.

3. **Run the script**  
   This will:
   - Connect to IBKR API
   - Request market data for a stock (e.g., AAPL)
   - Display the bid/ask price
   - Place a market buy order
   - Print the status of the order

---

## 📌 Notes

- Always start with a **paper trading** account to avoid unintended real trades.
- Use a unique `clientId` if running multiple scripts.
- This example uses **market orders** — which execute immediately at available price. Use limit orders for more control.

---

## 📈 Future Improvements (Ideas)

- Add support for limit, stop, and bracket orders
- Monitor and manage portfolio positions
- Schedule or trigger trades based on signals
- Add logging, error handling, and retry logic
- Integrate with a backtesting engine

---

## 🧑‍💻 Author

Developed by Kamran — a trading bot developer focused on automated strategies, real-time data, and financial APIs.

---

## 📄 License

This project is licensed under the MIT License.
