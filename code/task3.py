import time

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
def f1():
    res = ""
    for i in range(10**6):
        res += " "

@timer
def f2():
    res = " " * 10**6

# Приклад викликів функцій
f1()
f2()
