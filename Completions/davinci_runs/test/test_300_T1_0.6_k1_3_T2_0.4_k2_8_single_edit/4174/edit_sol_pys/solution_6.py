import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[0])
    print(a[-1])

if __name__ == '__main__':
    main()
