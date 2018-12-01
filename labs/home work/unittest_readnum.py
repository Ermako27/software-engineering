def readnum(string):  # формирование массива чисел из строки
    if string == None:
        return -1
    if type(string) != str:
        return -1
    if string == "":
        return -1
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

def test():
    err_count = 0

    # неверные аругменты

    if readnum(1234) != -1:
        err_count += 1
    if readnum(None) != -1:
        err_count += 1
    if readnum("") != -1:
        err_count += 1

    # некоторые верные тесты

    if readnum("0.5 12 30 aa") != ['12','30']:
        err_count += 1
    if readnum('246 432') != ['246','432']:
        err_count += 1
    if readnum('a b c d') != []:
        err_count += 1

    if err_count == 0:
        print('OK')
    else:
        print('Failed')


test()