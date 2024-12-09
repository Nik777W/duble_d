# Реализуйте генераторную функцию flatten(), которая принимает один аргумент:
# nested_list — список, элементами которого являются целые числа или списки,
# элементами которых, в свою очередь, также являются либо целые числа, либо списки; вложенность может быть произвольной
# Функция должна возвращать генератор, порождающий все числа, содержащиеся в nested_list, включая все числа из
# всех вложенных списков, а затем возбуждает исключение StopIteration.


def flatten(datas):
    rez = []
    def inner(data):
        if type(data) == int:
                rez.append(data)
        if type(data) == list:
            for i in data:
                inner(i)
        return rez
    inner(datas)
    yield from rez

# ТЕСТ__1             1 2 3 4 5
generator = flatten([[1, 2], [[3]], [[4], 5]])
print(*generator)

# ТЕСТ__2             1 2 3 4 5 6 7
generator = flatten([1, 2, 3, 4, 5, 6, 7])
print(*generator)