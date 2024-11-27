# Реализуйте класс Xrange, порождающий итераторы, конструктор которого принимает три аргумента в
# следующем порядке:
#
# start — целое или вещественное число
# end — целое или вещественное число
# step — целое или вещественное число, по умолчанию имеет значение 1
#
# Итератор класса Xrange должен генерировать последовательность членов арифметической прогрессии
# от start до end, включая start и не включая end, с шагом step, а затем возбуждать исключение StopIteration.

class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        result = self.start
        if self.step > 0:
            if self.start < self.end:
                self.start += self.step
                return result
            else:
                raise StopIteration
        if self.step < 0:
            if self.start > self.end:
                self.start += self.step
                return result
            else:
                raise StopIteration


# ТЕСТ__1            0 2 4 6 8


evens = Xrange(0, 10, 2)

print(*evens)


# ТЕСТ__2          10 9 8 7 6 5 4 3 2

xrange = Xrange(10, 1, -1)

print(*xrange)


# ТЕСТ__3           0.0; 0.5; 1.0; 1.5; 2.0; 2.5

xrange = Xrange(0, 3, 0.5)

print(*xrange, sep='; ')