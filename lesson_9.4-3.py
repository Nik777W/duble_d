# Реализуйте функцию polynom(), которая принимает один аргумент:
#
# x — вещественное число
# Функция должна возвращать значение выражения x**2+1
#
# Также функция должна иметь атрибут values, представляющий собой множество (тип set) всех значений функции,
# которые уже были вычислены.


def polynom(num):
    i = num**2+1
    polynom.values.add(i)
    return i

polynom.values = set()


# ТЕСТ__1

polynom(1)
polynom(2)
polynom(3)

print(*sorted(polynom.values))

# ТЕСТ__2
#
# print(polynom(5))
# print(polynom.values)
#
# ТЕСТ__3
#
# for _ in range(10):
#     polynom(10)
#
# print(polynom.values)