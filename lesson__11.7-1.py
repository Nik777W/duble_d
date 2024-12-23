# HTML-элементы — основа языка HTML. Каждый HTML-элемент обозначается начальным (открывающим) и конечным
# (закрывающим) тегами. Открывающий и закрывающий теги содержат имя элемента. Открывающий тег может
# содержать дополнительную информацию — атрибуты и значения атрибутов:
# <b>BeeGeek</b> <a href="https://stepik.org">Stepik</a>
# В примере выше тег <b> не содержит никаких атрибутов, а тег <a> содержит атрибут href со значением https://stepik.org.
# Напишите программу, которая находит во фрагменте HTML-страницы все атрибуты каждого тега.
# Формат входных данных
# На вход программе подается произвольное количество строк, которые образуют фрагмент HTML-страницы.
# Формат выходных данных
# Программа должна найти в введенном фрагменте HTML-страницы все теги и вывести их, указав для каждого соответствующие
# атрибуты. Теги вместе со всеми атрибутами должны быть расположены каждый на отдельной строке, в следующем формате:
# <тег>: <атрибут>, <атрибут>, ...
# Теги, а также атрибуты тегов, должны быть расположены в лексикографическом порядке.


from sys import stdin
from re import findall

d = {}
for i in stdin.readlines():
    a = findall(r'<([^/].*?)\b|[ ]([\w-]*?)=', i)
    x = ''
    for i in a:
        if i[0]:
            x = i[0]
            d[x] = []
        elif i[1]:
            d.setdefault(x, []).append(i[1])
for i in sorted(d):
    print(i, end=': ')
    print(*sorted(d[i]), sep=', ')


# TECT__1

# <p><a href="https://stepik.org">Stepik</a></p>
# <div class="catalog"><a href="https://stepik.org/catalog">Study hard. Teach harder</a></div>

# OТВЕТ:
# a: href
# div: class
# p:

# TECT__2
# <div id="oldie-warning" class="do-not-print">
#     <p>
#         <strong>Notice:</strong> Your browser is <em>ancient</em>. Please
#         <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.
#     </p>
# </div>

# OТВЕТ:
# a: href
# div: class, id
# em:
# p:
# strong:
