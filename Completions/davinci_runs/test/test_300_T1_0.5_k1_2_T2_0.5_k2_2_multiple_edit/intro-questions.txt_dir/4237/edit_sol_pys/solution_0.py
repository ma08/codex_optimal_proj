
import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    l = []

    for i in range(a, b+1):
        l.append(i)

    print(l)

if __name__ == '__main__':
    main()
