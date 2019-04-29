# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, arr):
    arr2 = []
    for x in arr:
        if func(x):
            arr2.append(x)

    return arr2


print(my_filter(lambda x: x > 4, [1, 8, 2, 34, 0]))
