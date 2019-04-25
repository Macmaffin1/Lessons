# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(number):
    number = str(number)
    number_1 = len(number)

    if number_1 != 6:
        return False

    a = number[:3]
    b = number[3:]
    a_1 = list(map(int, a))
    b_1 = list(map(int, b))

    if sum(a_1) == sum(b_1):
        return True
    else:
        return False
