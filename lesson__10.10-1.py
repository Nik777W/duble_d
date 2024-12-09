# Реализуйте функцию ncycles(), которая принимает два аргумента в следующем порядке:
# iterable — итерируемый объект
# times — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого
# объекта iterable, зацикленных times раз.
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны
# располагаться в своем исходном порядке.


from itertools import tee, chain

def ncycles(iterable, times):
    a = chain.from_iterable(tee(iterable, times))
    yield from a



# ТЕСТ__1             1 1 1 1 1 1 1 1 1 1
iterator = iter([1])
print(*ncycles(iterator, 10))

# ТЕСТ__2              b e e b e e b e e b e e
iterator = iter('bee')
print(*ncycles(iterator, 4))