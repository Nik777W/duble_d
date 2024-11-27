# Реализуйте функцию get_min_max(), которая принимает один аргумент:
#
# iterable — итерируемый объект, элементы которого сравнимы между собой
# Функция должна возвращать кортеж, в котором первым элементом является минимальный элемент итерируемого
# объекта iterable, вторым — максимальный элемент итерируемого объекта iterable. Если итерируемый объект iterable
# пуст, функция должна вернуть значение None.

def get_min_max(iterable):
    try:
        my_iter = iter(iterable)
        n_min = n_max = next(my_iter)
        for i in my_iter:
            if i > n_max:
                n_max = i
            if i < n_min:
                n_min = i
        return n_min, n_max
    except StopIteration:
        return None


# ТЕСТ__1            (0,9)

iterable = iter(range(10))
print(get_min_max(iterable))

# ТЕСТ__2             None

iterable = iter([])
print(get_min_max(iterable))

# ТЕСТ__3              (0, 99999999)

data = iter(range(100_000_000))
print(get_min_max(data))
