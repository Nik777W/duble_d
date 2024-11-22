# Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:
#
# values — список чисел
# group — список, кортеж или множество чисел
# Функция должна сортировать по не убыванию список чисел values, делая при этом приоритетной
# группу чисел из group, которая должна следовать первой.
#


def sort_priority(values, group):
    values.sort()
    def inner(gr):
        nonlocal values
        for i in sorted(gr, reverse=True):
            if i in values:
                values.remove(i)
                values.insert(0,i)
        return values
    inner(group)
    return inner



# ТЕСТ

numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])

print(numbers)

# ТЕСТ__2   [2, 3, 5, 7, 1, 4, 6, 8]

# numbers = [8, 3, 1, 2, 5, 4, 7, 6]
# group = {5, 7, 2, 3}
# sort_priority(numbers, group)
#
# print(numbers)