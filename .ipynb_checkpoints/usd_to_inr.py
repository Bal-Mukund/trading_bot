from forex_python.converter import CurrencyRates

currency1 = "USD"
currency2 = "INR"


c = CurrencyRates()

price = c.get_rate(currency1,currency2)

print(price)