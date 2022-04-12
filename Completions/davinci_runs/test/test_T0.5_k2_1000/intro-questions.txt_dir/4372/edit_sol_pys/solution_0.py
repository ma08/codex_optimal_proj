

def main():
    n = int(input())
    a = [int(i) for i in input().split()]

    if n == 1:
        print(1, a[0])
        return

    a.sort()

    i = 0
    while i < n and a[i] == 0:
        i += 1

    if i == n:
        print(1, a[0])
        return

    if i == n - 1:
        print(1, a[i])
        return

        return

    x = a[i]
    y = 1
    while i < n and a[i] == x:
        i += 1

    for j in range(i, n):
        if a[j] % x != 0:
            print(1, a[j])
            return

        y = max(y, a[j] // x)

    print(y, z)


main()
