def binary(num):  # перевод в 2 систему + доп код
    if num == None:
        return -1
    if type(num) != str:
        return -1
    if num == "":
        return -1
    otr_bin = ""
    dopkod = ""
    count = 1
    new_str = ""
    bin_str = ""
    num = int(num)
    flag = 0
    if num < 0:  # определение знака числа
        flag = 1
        num *= -1
    while num != 1:  # остатки от деления
        ost = num % 2
        bin_str += str(ost)  # неперевёрнутая строка
        num = num // 2
        count += 1
    bin_str += "1"  # добавление последней единицы
    for i in range(count - 1, -1, -1): # реверсирование строки
        new_str += bin_str[i]
    if flag == 0:  # если число было положительное
        return new_str
    else:  # иначе доп код
        for elem in new_str:
            if elem == "0":
                dopkod += "1"
            if elem == "1":
                dopkod += "0"
        m_dopkod = []
        for i in range(count):
            m_dopkod.append(dopkod[i])
        for i in range(count - 1, -1, -1):
            if m_dopkod[i] == "1":
                m_dopkod[i] = "0"
            elif m_dopkod[i] == "0":
                m_dopkod[i] = "1"
                break
        for elem in m_dopkod:
            otr_bin += elem
        return otr_bin

def test():
    err_count = 0

    # неверные аругменты

    if binary(1234) != -1:
        err_count += 1
    if binary(None) != -1:
        err_count += 1
    if binary("") != -1:
        err_count += 1

    # некоторые верные тесты

    if binary("468") != "111010100":
        err_count += 1
    if binary("-783") != "0011110001":
        err_count += 1
    if binary("246") != "11110110":
        err_count += 1

    if err_count == 0:
        print('OK')
    else:
        print('Failed')

test()