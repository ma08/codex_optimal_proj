

import sys

input = sys.stdin.readline()

input = input.split(" ")

X = int(input[0])
K = int(input[1])
D = int(input[2])

if X < 0:
    X = -X

if K <= X / D:
    print(X - K * D)
else:
    K -= X / D
    K %= 2
    if K == 0:
        print(X % D)
    else:
        print(D - X % D)