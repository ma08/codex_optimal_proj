
import sys
readline = sys.stdin.buffer.readline

def main():
    n = int(readline())
    a = list(map(int, readline().split()))
    a.sort()
    print(a[n-1] - a[n-2])

if __name__ == '__main__':
    main()
