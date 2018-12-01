from iarray import *

def test_1():
  arr = list()
  
  arr.append(0)
  arr.append(-1)
  arr.append(3)
  arr.append(-2)
  arr.append(5)
  
  return arr, 5

def test_2():
  arr = list()

  arr.append(-1)
  arr.append(-11)
  arr.append(3)
  arr.append(2)
  arr.append(5)

  return arr, 5


def main():
  arr, n = test_1()
  arr_t2, n_t2 = test_2()

  print("Source")
  print_array(arr, n)
  print_array(arr_t2, n_t2)
  
  new_arr, new_n = form_array(arr, n)
  new_arr_t2, new_n_t2 = form_array(arr_t2, n_t2)

  print("Result")
  print_array(new_arr, new_n)
  print_array(new_arr_t2, new_n_t2)


if __name__ == '__main__':
  main()
  
