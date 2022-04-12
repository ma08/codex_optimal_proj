import sys

def main():
    n, m = map(int, input().split())
    lookup = {}
    for _ in range(n):
        a, b = input().split()
        lookup[a] = b
    for _ in range(m):
        a, b = input().split()
        if len(a) != len(b):
            print("no")
            continue
        for i in range(len(a)):
            if a[i] not in lookup or lookup[a[i]] != b[i]:
                print("no")
                break
        else:
            print("yes")

main()
