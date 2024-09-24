'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №4.2
Домашняя работа по уроку "Пространство имен."
'''

# Задание функций
def test_function():
    global inner_function #Требуется объявить функцию глобальной, чтобы обратиться к ней из глобальной части кода
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

# Блок вызовов функций
test_function()

# Без объявления функции, как глобальная - выдается ошибка:
# "NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?"
inner_function()
