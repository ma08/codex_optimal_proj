

from sys import stdin

def main():
    n, k = map(int, stdin.readline().split())
    a = [0] * n
    for i in range(k):
        d = int(stdin.readline())
        for j in map(int, stdin.readline().split()):
            a[j - 1] += 1
    print(a.count(0))

if __name__ == '__main__':
    main()