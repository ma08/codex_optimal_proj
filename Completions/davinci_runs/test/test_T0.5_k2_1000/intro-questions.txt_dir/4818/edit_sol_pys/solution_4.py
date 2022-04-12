
def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(m):
        if b[i] in a:
            print(b[i])
            a.remove(b[i])
    for i in range(n):
        if a[i] not in b:
            print(a[i])

main()
