# Напишите программу, которая переопределяет встроенную функцию print() так, чтобы она печатала все переданные
# строковые аргументы в верхнем регистре.
#
# Примечание 1. Значения sep и end также должны переводиться в верхний регистр.

temp = print

def print(*args,sep=' ',end=''):
    temp(*[i.upper() if isinstance(i, str) else i for i in args], sep=sep.upper(), end=end.upper())


# ТЕСТ!!!__1

print('bee', 'geek', sep=' and ', end=' wow')

# ТЕСТ!!!__2

words = ['a', 2, 'b', 3, ['1a', '2a', '3a', '4a'], '5A', True, 8.763, ('python', 'c++')]
kwarg = {'sep' : ',f ', 'end' : ' Finish'}
print(*words, **kwarg)