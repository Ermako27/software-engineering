@echo off
main_test.py < in_1.txt
fc new_file.txt out_1.txt

main_test.py < in_2.txt
fc new_file.txt out_2.txt

main_test.py < in_3.txt
fc new_file.txt out_3.txt

main_test.py < in_4.txt > out.txt
fc out.txt out_4.txt

main_test.py < in_5.txt > out.txt
fc out.txt out_5.txt
pause