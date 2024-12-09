# Реализуйте декоратор retry, который принимает один аргумент:
# times — натуральное число
# Декоратор должен выполнять повторную попытку вызова декорируемой функции, если во время
# ее выполнения возникает ошибка. Декоратор должен вызывать ее до тех пор, пока не исчерпает
# количество попыток times, после чего должен возбуждать исключение MaxRetriesException.
# Также декоратор должен сохранять имя и строку документации декорируемой функции.


from functools import wraps


class MaxRetriesException(Exception):
    pass

def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.num += 1
            try:
                return func(*args, **kwargs)
            except:
                if wrapper.num < times:
                    return wrapper(*args, **kwargs)
                else:
                    raise MaxRetriesException
        wrapper.num = 0
        return wrapper
    return decorator


# ТЕСТ__1   <class '__main__.MaxRetriesException'>
@retry(3)
def no_way():
    raise ValueError
try:
    no_way()
except Exception as e:
    print(type(e))


# ТЕСТ__2     beegeek
@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')


beegeek()
