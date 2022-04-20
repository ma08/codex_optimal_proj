
import sys

def main():
    n, m = list(map(int, input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(a)

if __name__ == '__main__':
    main()
