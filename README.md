# Currency Exchange Rate Application

This is a Python application that fetches current exchange rates using the Exchange Rate API. The application implements the Singleton design pattern to ensure only one instance of the exchange rate service is created.

## Features

- Implements Singleton pattern for efficient resource management
- Fetches real-time currency exchange rates
- Simple and clean API interface
- Error handling for API requests

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Stustan/currency_rates.git
cd currency_rates
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from currency_exchange import CurrencyExchange

# Get instance of CurrencyExchange
exchange = CurrencyExchange()

# Get exchange rates for USD
rates = exchange.get_exchange_rate("USD")

# Print rates
print(rates)
```

## Requirements

- Python 3.6+
- requests library

## License

This project is open source and available under the MIT License. 