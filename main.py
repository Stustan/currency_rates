from currency_exchange import CurrencyExchange

def main():
    # Создаем первый экземпляр
    exchange1 = CurrencyExchange()
    
    # Пробуем создать второй экземпляр (должен вернуть тот же объект)
    exchange2 = CurrencyExchange()
    
    # Проверяем, что это один и тот же объект
    print(f"Are instances the same? {exchange1 is exchange2}")
    
    # Получаем курсы валют для USD
    rates = exchange1.get_exchange_rate("USD")
    
    if rates:
        print("\nExchange rates for USD:")
        for currency, rate in rates.get('rates', {}).items():
            print(f"{currency}: {rate}")

if __name__ == "__main__":
    main() 