
import sys

def main():
    n = int(input())
    total = 0
    for i in range(n):
        a, b = input().split()
        if b == 'JPY':
            total += float(a)
        else:
            total += float(a) * 380000.0
    print(total)
    return

if __name__ == '__main__':
    main()
