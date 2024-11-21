# Реализуйте функцию numbers_sum(), которая принимает один аргумент:
#
# elems — список произвольных объектов
# Функция должна возвращать сумму чисел (типы int и float), находящихся в списке elems,
# игнорируя все нечисловые объекты. Если в списке elems нет чисел, функция должна
# вернуть число 0.
#
# Также функция должна иметь следующую строку документации:
#
# Принимает список и возвращает сумму его чисел (int, float),
# игнорируя нечисловые объекты. 0 - если в списке чисел нет.

def numbers_sum(elems):
    '''Принимает список и возвращает сумму его чисел (int, float),
    игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    return sum(filter(lambda x: isinstance(x, (float, int)), elems))



print(numbers_sum([1, '2', 3, 4, 'five']))

print(numbers_sum.__doc__)
print(numbers_sum(['beegeek', 'stepik', '100']))