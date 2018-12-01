from iarray import *

def Test1():
  Arr = list()
  
  Arr.append(5)
  Arr.append(3)
  Arr.append(2)
  Arr.append(5)
  Arr.append(1)
  
  return Arr, 5

def Test2():
  Arr = list()
  
  Arr.append(5)
  Arr.append(5)
  Arr.append(5)
  Arr.append(5)
  Arr.append(6)
  
  return Arr, 5



def main():
  Arr, N = Test1()
  Arr_t2 , N_t2 = Test2()
  
  
  print("Maximal value is found " + str(GetMaxCount(Arr, N)) + " times.")
  print("Function return " + str(GetMaxCount(Arr_t2, N_t2)) + " in fact 1.")

if __name__ == '__main__':
  main()
