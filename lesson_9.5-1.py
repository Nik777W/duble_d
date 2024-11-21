# Нередко в разных странах используются разные форматы дат. Рассмотрим часть из них:
#
# код страны	формат даты
# ru	DD.MM.YYYY
# us	MM-DD-YYYY
# ca	YYYY-MM-DD
# br	DD/MM/YYYY
# fr	DD.MM.YYYY
# pt	DD-MM-YYYY
# Реализуйте функцию date_formatter(), которая принимает один аргумент:
#
# country_code — код страны
# Функция date_formatter() должна возвращать функцию, которая принимает в качестве аргумента дату (тип date) и
# возвращает строку с данной датой в формате страны с кодом country_code.
#
# Примечание 1. Гарантируется, что в функцию date_formatter() передаются только те коды стран, что
# перечислены в приведенной выше таблице.


from datetime import date

def date_formatter(country_code: str):
    def inner(my_date):
        d = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y', 'ca': '%Y-%m-%d',
             'br': '%d/%m/%Y', 'pt': '%d-%m-%Y', 'fr': '%d.%m.%Y'
             }
        return my_date.strftime(d[country_code])
    return inner



# ТЕСТ


date_ru = date_formatter('ca')
today = date(2022, 1, 25)
print(date_ru(today))
