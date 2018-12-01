from functions import *
import os

try:
    f = open("file.txt", "r")
    new_f = open("new_file.txt", "w")
except FileNotFoundError:
    print("файл не существует")

else:
    if os.stat("file.txt").st_size == 0:
        print("файл пуст")
    else:
        for elem in f:
            str_mass = ""
            s = readnum(elem)
            #print(s)
            for num in s:
                flag = sumfigures(num)
                #print(flag)
                if flag % 2 != 0:
                    str_mass += revers(num) + " "
                    #print(str_mass)

                elif flag != 0 and flag % 2 == 0:
                    str_mass += binary(num) + " "
                if flag == 0: # если сумма чисел 0 то
                    str_mass += num + " "

            if str_mass != "":
                new_f.write(str_mass + "\n")
    f.close()
    new_f.close()



