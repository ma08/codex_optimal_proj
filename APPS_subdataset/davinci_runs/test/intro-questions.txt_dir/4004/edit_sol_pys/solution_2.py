

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    if n == 1:
        print(0)
        return
    if a[0] == a[n-1]:
        print(0)
        return
    if a[0] + 1 == a[1] or a[n-2] + 1 == a[n-1] or (a[0] == a[1] and a[n-2] + 1 == a[n-1]):
        print(1)
        return
    print(-1)

main()
