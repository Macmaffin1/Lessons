# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

__author__ = 'Мельник Виктория'
variable_1 = input('Введите значение 1 ')
variable_2 = input('Введите значение 2 ')
variable_1, variable_2 = variable_2, variable_1
print(variable_1, variable_2)
