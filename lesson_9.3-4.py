# Используя синтаксис анонимных функций, реализуйте рекурсивную функцию fib(), которая принимает один аргумент:
#
# n — натуральное число
# Функция должна возвращать n-ый член последовательности Фибоначчи.
# 1,1,2,3,5,8,13,21,34,55,89,144,233,...

fib = lambda n: 1 if n == 1 or n ==2 else (fib(n-1) + fib(n - 2))

print(fib(11))
