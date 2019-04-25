# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fib(n, m):
    a = [1, 1]
    for x in range(m):
        a_1 = a[-1] + a[-2]
        a.append(a_1)

    return a[n:m +1]


fibonachi = fib(5, 12)
print(fibonachi)
