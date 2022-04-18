
import sys

def main():
    n = int(sys.stdin.readline())
    sum = 0
    for i in range(n):
        x, u = sys.stdin.readline().split()
        if u == 'JPY':
            sum += float(x)
        else:
            sum += float(x) * 380000.0
    print(sum)
    return 0

if __name__ == '__main__':
    main()
