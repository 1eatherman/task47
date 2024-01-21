def convert_to_uah(func):
    def wrapper(count, price):
        print("check=|count|price|")
        summa = count * price
        return f"{summa} UAH"
    return wrapper

def convert_to_currency(currency_rate):
    def decorator(func):
        def wrapper(count, price):
            result_in_uah = func(count, price)
            summa_in_uah = float(result_in_uah.split()[0])
            summa_in_currency = summa_in_uah / currency_rate
            return f"{summa_in_currency:.2f} USD"
        return wrapper
    return decorator

@convert_to_uah
def check(count, price):
    summa = count * price
    return f"{summa} UAH"

# Приклад використання:
print(check(2, 10))

# Декорування з конвертацією в іншу валюту
@convert_to_currency(currency_rate=37.8)
def decor_check(count, price):
    return check(count, price)

# Приклад використання з конвертацією в іншу валюту
print(decor_check(2, 10))
