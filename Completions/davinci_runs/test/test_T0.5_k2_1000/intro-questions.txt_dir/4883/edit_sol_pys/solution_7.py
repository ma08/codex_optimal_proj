
import sys

def main():
    m, n = map(int, input().split())
    d = {}
    for i in range(m):
        a, b = input().split()
        if a not in d:
            d[a] = [b]
        else:
            d[a].append(b)
    for i in range(n):
        a, b = input().split()
        if len(a) != len(b):
            print("no")
            continue
        if a[0] in d:
            if b[0] in d[a[0]]:
                print("yes")
            else:
                print("no")
                break
        else:
            print("yes")

main()
