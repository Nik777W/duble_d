# Реализуйте функцию remove_marks(), которая принимает два аргумента в следующем порядке:
#
# text — произвольная строка
# marks — набор символов
# Функция должна возвращать строку text, предварительно удалив из нее все символы, перечисленные в строке marks.
#
# Также функция remove_marks() должна иметь атрибут count, представляющий собой количество вызовов данной функции.

def remove_marks(text, marks):
    a = "".join(filter(lambda x: x not in marks, text))
    remove_marks.__dict__['count'] = remove_marks.__dict__.setdefault('count',0) + 1
    return a


# ТЕСТ__1
#
# text = 'Hi! Will we go together?'
#
# print(remove_marks(text, '!?'))
# print(remove_marks.count)
#
# ТЕСТ__2

marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))

print(remove_marks.count)