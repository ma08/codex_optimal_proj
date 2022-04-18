
import sys

n = int(sys.stdin.readline())

if n % 25 == 0:
    print(0)
else:
    num = str(n)
    num = list(num)
    length = len(num)
    pos = 0
    while pos < length - 1:
        if num[pos] == '0' and num[pos + 1] != '0':
            num[pos], num[pos + 1] = num[pos + 1], num[pos]
            pos += 2
        else:
            pos += 1
    num = ''.join(num)
    if int(num) % 25 == 0:
        print(length - len(num))
    else:
        print(-1)
