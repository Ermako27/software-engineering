def sumfigures(num):  # сумма цифр числа
    if num == None:
        return -1
    if type(num) != str:
        return -1
    if num == "":
        return -1
    summ = 0
    for elem in num:
        if elem != "-":
            summ += int(elem)
    return summ


def test():
    err_count = 0

    # неверные аругменты

    if sumfigures(1234) != -1:
        err_count += 1
    if sumfigures(None) != -1:
        err_count += 1
    if sumfigures("") != -1:
        err_count += 1

    # некоторые верные тесты

    if sumfigures("123") != 6:
        err_count += 1
    if sumfigures("-123") != 6:
        err_count += 1
    if sumfigures("1111") != 4:
        err_count += 1
    if sumfigures("000") != 0:
        err_count += 1

    if err_count == 0:
        print('OK')
    else:
        print('Failed')

test()