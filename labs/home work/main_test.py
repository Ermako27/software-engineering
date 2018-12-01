from functions import *
import os

try:
    file = input("input name of file: ")
    f = open(file, "r")
    new_f = open("new_file.txt", "w")
except FileNotFoundError:
    print("no existing file")

else:
    if os.stat(file).st_size == 0:
        print("empty file")
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



