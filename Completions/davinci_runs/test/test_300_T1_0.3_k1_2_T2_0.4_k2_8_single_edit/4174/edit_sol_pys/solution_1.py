
import sys

def main():
    n, x = map(int, sys.stdin.readline().split())
    l = list(map(int, sys.stdin.readline().split()))
    d = [0]
    for i in range(n):
        d.append(d[i] + l[i])
    print(len(list(filter(lambda a: a <= x, d))))

if __name__ == '__main__':
    main()
