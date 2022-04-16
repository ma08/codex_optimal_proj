# coding: utf-8

A, B, C = sorted(map(int, input().split()))
order = input()
print('{} {} {}'.format(eval(order[0]), eval(order[1]), eval(order[2])))
