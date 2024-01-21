from functools import wraps

def check_inputs(func):
    @wraps(func)
    def wrapper(a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            print("Помилка: Обидва аргументи повинні бути числовими.")
            return None
        elif b == 0:
            print("Помилка: Ділення на нуль недопустиме.")
            return None
        else:
            return func(a, b)
    return wrapper

@check_inputs
def divide(a: float, b: float) -> float:
    print('виконується ділення')
    return a / b

result = divide(10, 2)
if result is not None:
    print(f"Результат: {result}")
