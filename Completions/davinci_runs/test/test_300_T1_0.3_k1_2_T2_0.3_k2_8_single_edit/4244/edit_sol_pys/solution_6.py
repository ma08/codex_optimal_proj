
import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(i) for i in sys.stdin.readline().split()]
    a.sort()
    m = a[0]
    for i in range(1, n): m = (m + a[i]) / 2
    print(sum([(i - m) ** 2 for i in a]))

if __name__ == '__main__':
    main()
