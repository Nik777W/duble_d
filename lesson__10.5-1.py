# Реализуйте генераторную функцию primes(), которая принимает два аргумента в следующем порядке:
# left — натуральное число
# right — натуральное число
# Функция должна возвращать генератор, порождающий последовательность простых чисел от left до right включительно,
# а затем возбуждающий исключение StopIteration.
# Примечание 1. Гарантируется, что left <= right.


def primes(left, right):
    while left <= right:
        coun = 0
        for i in range(2, left+1):
            if left % i == 0:
                coun += 1
                if coun >1:
                    break
        if coun == 1:
            yield left
        left += 1


# ТЕСТ__1              2 3 5 7 11 13
generator = primes(1, 15)
print(*generator)

# ТЕСТ__2              7
#                      11
generator = primes(6, 36)
print(next(generator))
print(next(generator))