import time

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції {func.__name__} з аргументами {args}")
        result = func(*args, **kwargs)
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Функція {func.__name__} виконана за {elapsed_time:.5f} секунд")
        return result
    return wrapper

@timer
@log
def even_nums(a, b):
    return [num for num in range(a, b+1) if num % 2 == 0]

# Приклад використання:
result = even_nums(1, 10)
print("Парні числа:", result)
