def readnum(string):  # формирование массива чисел из строки
    string += " "
    nums = []
    num = ""
    template = ".-1234567890"
    for elem in string:
        if elem in template:
            num += elem
        if elem == " " and num != "":
            if "." not in num:
                nums.append(num)
            num = ""
    return nums


def sumfigures(num):  # сумма цифр числа
    summ = 0
    for elem in num:
        if elem != "-":
            summ += int(elem)
    return summ


def revers(num):
    count = 0
    revnum = ""
    flag = 0
    num = int(num)
    if num < 0:
        flag = 1
        num *= -1
    while num != 0:
        figure = num % 10
        revnum += str(figure)
        num = num // 10
    if revnum[0] == "0":
        for elem in revnum:
            if elem == "0":
                count += 1
            else:
                break
    revnum = revnum[count:]

    if flag:
        revnum = "-" + revnum

    return revnum


def binary(num):  # перевод в 2 систему + доп код
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


if __name__ == "__main__":
    #print(readnum('a b c d'))
    print(sumfigures(""))
    #print(revers(""))
    #print(double("246"))
    #print(binary("-1"))
