

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = []
    for x in range(n-1, -1, -1):
        if a[x] not in b:
            b.append(a[x])
    print(len(b))
    print(*b[::-1])

main()