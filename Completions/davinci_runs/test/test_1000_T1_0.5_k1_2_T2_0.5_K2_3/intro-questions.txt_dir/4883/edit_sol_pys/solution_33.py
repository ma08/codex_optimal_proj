
import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    d = dict()
    for i in range(m):
        a, b = sys.stdin.readline().split()
        d[a] = b
    for i in range(n):
        a, b = sys.stdin.readline().split()
        if len(a) != len(b):
            print("no")
            continue
        a = list(a)
        b = list(b)
        for i in range(len(a)):
            if a[i] in d:
                if b[i] not in d[a[i]]:
                    print("no")
                    break
        if a[i] not in d:
                print("no")
                break
        else:
            print("yes")

main()
