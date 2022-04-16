
import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    d = dict()
    for i in range(m):
        a, b = sys.stdin.readline().split()
        if a not in d:
            d[a] = set(b)
        else:
            d[a].add(b)
    for i in range(n):
        a, b = sys.stdin.readline().split()
        if len(a) != len(b):
            print("no")
            continue
        for j in range(len(a)):
            if a[j] in d:
                if b[j] not in d[a[j]]:
                    print('no')
                    break;
            else:
                print('no')
                break;
        else:
            print('yes')

main()
