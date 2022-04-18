

def main():
    n = int(input())
    a = [int(i) for i in input().split()]

    if n == 1:
        print(1, a[0], sep=" ")
        return

    a.sort()

    i = 0
    while i < n and a[i] == 0:
        i += 1

    if i == n:
        print(1, a[-1], sep=" ")
        return

    if i == n - 1:
        print(1, a[i], sep=" ")
        return

    z = a[i]
    y = 1
    while i < n and a[i] == z:
        i += 1

    for j in range(i, n):
        if a[j] % z != 0:
            print(1, a[j], sep=" ")
            return

        y = max(y, a[j] // z)

    print(y, z, sep=" ")


main()
