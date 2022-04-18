

import sys

def main():
    # Reading input
    a = [int(x) for x in sys.stdin.readline().split()] # прочитать из стандартного потока ввода построчно и преобразовать в числа
    
    # Computing and printing answer
    print(min(a)) # вывести в стандартный поток вывода минимальное число из массива
    
if __name__ == '__main__':
    main()
