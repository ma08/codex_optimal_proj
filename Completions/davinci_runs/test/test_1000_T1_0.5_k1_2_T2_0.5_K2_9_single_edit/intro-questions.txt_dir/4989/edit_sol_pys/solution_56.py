

import math

def main():
    n = int(input())
    a = [int(i) for i in input().split()]

Alice = 0
Bob = 0

for i in range(n):
    if i % 2 == 0:
        Alice += a[n - i - 1]
    else:
        Bob += a[n - i - 1]

print(Alice, Bob)
