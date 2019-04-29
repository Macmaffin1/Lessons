# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

A1 = (2, 3)
A2 = (7, 9)
A3 = (4, 3)
A4 = (9, 9)

A3, A4 = A4, A3

def length(a1, a2):
    x1 = a1[0]
    x2 = a2[0]
    y1 = a1[1]
    y2 = a2[1]
    a = (x2 - x1)**2
    b = (y2 - y1)**2
    c = (a + b)**0.5
    return c


result1 = length(A1, A3)
result2 = length(A1, A2)
result3 = length(A3, A4)
result4 = length(A2, A4)

if result1 == result4 and result2 == result3:
    print("Параллелограмм")
else:
    result1 = length(A1, A4)
    result2 = length(A1, A2)
    result3 = length(A3, A4)
    result4 = length(A2, A3)
    if result1 == result4 and result2 == result3:
        print("Параллелограмм")
    else:
        print('Увы, нет')
