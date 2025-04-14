# Currency Exchange Rate Application

This is a Python application that fetches current exchange rates using the Exchange Rate API. The application implements the Singleton design pattern to ensure only one instance of the exchange rate service is created.

## Features

- Implements Singleton pattern for efficient resource management
- Fetches real-time currency exchange rates
- Interactive currency code input with validation
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

1. Run the application:
```bash
python main.py
```

2. Enter a three-letter currency code when prompted (e.g., USD, EUR, RUB)

3. The application will display exchange rates for all available currencies relative to your chosen currency.

Example output:
```
Введите трехбуквенный код валюты (например, USD, EUR, RUB): USD

Курсы валют относительно USD:
EUR: 0.92
GBP: 0.79
JPY: 150.12
...
```

## Requirements

- Python 3.6+
- requests library

## License

This project is open source and available under the MIT License. 