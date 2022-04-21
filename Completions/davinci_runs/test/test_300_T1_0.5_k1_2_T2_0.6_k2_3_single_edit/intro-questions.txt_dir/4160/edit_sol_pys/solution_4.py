#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Дано целое число N (> 1). Если оно является степенью числа 3, то вывести True,
# если не является — вывести False
#
# Формат ввода
# Вводится целое положительное число.
#
# Формат вывода
# Выведите ответ на задачу.
#
# Sample Input 1:
# 27
#
# Sample Output 1:
# True
#
# Sample Input 2:
# 1
#
# Sample Output 2:
# False


n = int(input())

while n % 3 == 0:
    n //= 3

if n == 1:
    print('True')
else:
    print('False')
