# coding: utf-8

# 以下のように、1からNまでの整数を使って、N = a*b + cとなる整数の組を数え上げるプログラムを作成してください。
#
# N = a*b + c
#
# ただし、a, b, cはそれぞれ1以上の整数であり、a <= bであるとします。
#
# また、入力はすべて整数とし、1 <= N <= 1000とします。
#
# Input
# N
#
# Output
# N = a*b + cとなる整数の組の数

N = int(input())

count = 0
for a in range(1, N+1):
    for b in range(1, N+1):
        c = N - a * b
        if c > 0:
            count += 1

print(count)
