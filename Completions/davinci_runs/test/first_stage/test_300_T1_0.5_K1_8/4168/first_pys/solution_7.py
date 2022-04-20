

import sys

N = int(input())

if N == 0:
    print(0)
    sys.exit()

result = []

while True:
    if N == 0:
        break
    elif N % 2 == 0:
        result.append(0)
        N = N // 2
    elif N % 2 == 1:
        result.append(1)
        N = N // 2
    elif N % 2 == -1:
        result.append(1)
        N = (N - 1) // 2
    else:
        result.append(0)
        N = (N + 1) // 2

print("".join(map(str, result[::-1])))