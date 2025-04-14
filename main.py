from currency_exchange import CurrencyExchange

def get_currency_input() -> str:
    """
    Get currency code from user input with validation
    """
    while True:
        currency = input("Введите трехбуквенный код валюты (например, USD, EUR, RUB): ").upper()
        if len(currency) == 3 and currency.isalpha():
            return currency
        print("Ошибка: введите корректный трехбуквенный код валюты")

def main():
    # Создаем экземпляр CurrencyExchange
    exchange = CurrencyExchange()
    
    # Получаем валюту от пользователя
    base_currency = get_currency_input()
    
    # Получаем курсы валют
    rates = exchange.get_exchange_rate(base_currency)
    
    if rates:
        print(f"\nКурсы валют относительно {base_currency}:")
        for currency, rate in rates.get('rates', {}).items():
            print(f"{currency}: {rate}")
    else:
        print("Не удалось получить курсы валют. Проверьте правильность введенного кода валюты.")

if __name__ == "__main__":
    main() 