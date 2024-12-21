# Реализуйте функцию multiple_split(), которая принимает два аргумента:
# string — строка
# delimiters — список строк
# Функция должна разбивать строку string на подстроки, используя в качестве разделителей строки из списка
# delimiters, и возвращать полученный результат в виде списка.
#
# Примечание 1. Другими словами, функция multiple_split() должна работать аналогично строковому методу split(),
# за тем исключением, что delimiters может содержать не единственный разделитель, а целый набор разделителей.

import re

def multiple_split(string, delimiters):
    d = []
    for i in delimiters:
        t=''
        for j in i:
            t+= '\\'+j
        d.append(t+'|')
    w = ''.join(d).rstrip('|')
    return re.split(rf'(?:{w})' , string)


# ТЕСТ__1
print(multiple_split('stepik_python-dima*roma*jenya-timur__arthur', ['_', '*', '#', '@']))
# ['stepik', 'python-dima', 'roma', 'jenya-timur', '', 'arthur']
# ТЕСТ__2
print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))
# ['Timur', 'Arthur', 'Dima', 'Anri']
# ТЕСТ__3
print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))
# ['timur', 'arthur', 'dima', 'anri', 'roma', 'ruslan']