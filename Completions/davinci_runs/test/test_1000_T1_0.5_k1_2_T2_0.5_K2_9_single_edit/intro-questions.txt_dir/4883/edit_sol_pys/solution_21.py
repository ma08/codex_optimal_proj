import sys

    sys.stdin = open("file.in", "r")
    sys.stdout = open("file.out", "w")
def main():
    m, n = map(int, sys.stdin.readline().split())
    d = {}
    for i in range(m):
        a, b = sys.stdin.readline().split(" ")
        if a not in d:
            d[a] = [b]
        else:
            d[a].append(b)
    for i in range(n):
        a, b = sys.stdin.readline().split(" ")
        if len(a) != len(b):
            print("no")
            continue
        a = list(a)
        b = list(b)
        for i in range(len(a)):
            if a[i] in d:
                if b[i] in d[a[i]]:
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
