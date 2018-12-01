def revers(num):
    if num == "":
        return -1
    if num == None:
        return -1
    if type(num) != str:
        return -1
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


def test():
    err_count = 0

    # неверные аругменты

    if revers(1234) != -1:
        err_count += 1
    if revers(None) != -1:
        err_count += 1
    if revers("") != -1:
        err_count += 1

    # некоторые верные тесты

    if revers("1234") != "4321":
        err_count += 1
    if revers("-1234") != "-4321":
        err_count += 1
    if revers("1111") != "1111":
        err_count += 1

    if err_count == 0:
        print('OK')
    else:
        print('Failed')

test()