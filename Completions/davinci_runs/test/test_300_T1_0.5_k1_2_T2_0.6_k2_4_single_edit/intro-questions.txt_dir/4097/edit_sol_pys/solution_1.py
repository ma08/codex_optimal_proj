
import sys

def main():
    n = int(sys.stdin.readline())
    arr = [int(i) for i in input().split()]
    a = 0
    b = 0
    c = 0
    count = 0
    for i in arr:
        if i == 1:
            a += 1
        elif i == 2:
            b += 1
        else:
            c += 1
    count += c
    count += b
    count += a // 2
    a %= 2
    if a == 1:
        if b == 0:
            count += 1
            a = 0
        else:
            count += 1
            a = 0
            b -= 1
    count += b // 2
    b %= 2
    if b == 1:
        if a == 0:
            count += 1
        else:
            count += 1
            a = 0
    if a == 1:
        count += 1
    print(count)

if __name__ == "__main__":
    main()
