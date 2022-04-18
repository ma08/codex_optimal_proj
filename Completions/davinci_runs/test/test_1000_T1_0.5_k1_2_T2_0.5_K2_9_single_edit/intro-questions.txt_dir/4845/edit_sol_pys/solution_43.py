

#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main():
    d, m = map(int, sys.stdin.readline().split()) # преобразование типа
    days = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"] # массив дней
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0 # начальное значение
    for i in range(m-1):
        day += months[i] # прибавление к значению дней в месяце
    day += d # вычисление дня недели по дате
    print(days[day % 7])

if __name__ == '__main__':
    main()
