# Реализуйте функцию print_operation_table(), которая принимает три аргумента в следующем порядке:
#
# operation — функция, характеризующая некоторую бинарную операцию
# rows — натуральное число
# cols — натуральное число
# Функция должна составлять и выводить таблицу из rows строк и cols столбцов, в которой элемент со строкой n и
# столбцом m имеет значение operation(n, m).
#
# Примечание 1. Нумерация строк и столбцов в таблице начинается с единицы.
# Примечание 2. Элементы в строках таблицы должны быть разделены одним пробелом, причем выравнивать таблицу необязательно.

def print_operation_table(operation, rows, cols):
    a= list(map(lambda x: list(range(cols)),range(rows)))
    for i in range(len(a)):
        for y in range(len(a[i])):
            a[i][y] = operation(i+1, y+1)
        print(*list(map(lambda x: str(x)+" ", a[i])))




print_operation_table(lambda a, b: a * b, 5, 5)
print_operation_table(pow, 5, 4)