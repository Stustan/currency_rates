import requests
from typing import Dict, Optional

class CurrencyExchange:
    _instance: Optional['CurrencyExchange'] = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.base_url = "https://api.exchangerate-api.com/v4/latest/"
            self.initialized = True
    
    def get_exchange_rate(self, base_currency: str) -> Dict:
        """
        Get exchange rates for the specified base currency
        
        Args:
            base_currency (str): The base currency code (e.g., 'USD', 'EUR')
            
        Returns:
            Dict: Dictionary containing exchange rates
        """
        try:
            response = requests.get(f"{self.base_url}{base_currency}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rates: {e}")
            return {} 