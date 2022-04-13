
import sys

def main():
    n = int(input())
    s = 0
    for i in range(n):
        x, u = input().split()
        if u == 'JPY':
            s += float(x)
        else:
            s += float(x) * 380000.0
    print(s)
    return

if __name__ == '__main__':
    main()
