'''
Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!).
Пример работы программы:
Ввод:                                           Вывод:
6                                               1 2 3
                                                4 5 6
                                                7 8 9
                                                10 11 12
                                                13 14 15
                                                16 17 18
'''
import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i*j, end=' ')
        print()

if __name__ == '__main__':
    main()
