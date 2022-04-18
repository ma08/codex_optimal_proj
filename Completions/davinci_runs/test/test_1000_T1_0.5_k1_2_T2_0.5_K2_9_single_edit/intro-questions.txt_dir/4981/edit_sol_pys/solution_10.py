import sys
sys.stdin = open('input.txt', 'r')

A, B, C = sorted(map(int, input().split()))
order = input()
print(eval(order[0]), eval(order[1]), eval(order[2]))
