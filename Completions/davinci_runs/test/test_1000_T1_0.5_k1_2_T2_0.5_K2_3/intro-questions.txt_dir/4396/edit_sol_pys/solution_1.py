
import sys

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = input().split()
        if b == 'JPY':
            sum += float(a)
        else:
            sum += float(a) * 380000.0
    print(sum)
    return

if __name__ == '__main__':
    main()
