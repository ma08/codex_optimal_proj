import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    d = {}
    for i in range(m):
        a, b = sys.stdin.readline().split()
        if a not in d:
            d[a] = [b]
        else:
            d[a].append(b)
    for j in range(n):
        a, b = sys.stdin.readline().split()
        if len(a) != len(b):
            print("no")
            continue
        a = list(a)
        b = list(b)
        for k in range(len(a)):
            if a[k] in d:
                if b[k] in d[a[k]]:
                    continue
                else:
                    print("no")
                    break
            else:
                print("no")
                break
        else:
            print("yes")

main()
