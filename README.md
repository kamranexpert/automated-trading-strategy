# Automated Trading Strategy (IBKR + Python)

This repository provides a basic example of an automated trading strategy using the `ib_insync` Python library to connect with Interactive Brokers' Trader Workstation (TWS) or IB Gateway.

It demonstrates how to:

- Connect to IBKR's API
- Request live market data
- Place a simple market order
- Print bid/ask prices and order status

---

## 🔧 Requirements

- Python 3.7+
- [Interactive Brokers TWS or IB Gateway](https://www.interactivebrokers.com/en/trading/tws.php)
- IBKR Paper or Live account
- API access enabled in TWS/Gateway

### Python Libraries

Install required packages:

```bash
pip install ib_insync
