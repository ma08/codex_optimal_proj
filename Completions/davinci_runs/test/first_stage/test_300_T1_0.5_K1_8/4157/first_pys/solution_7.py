

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    a.reverse()

    for i in range(n):
        if a[i] % 3 == 0:
            print(a[i], end = " ")
            a[i] = -1
            break
    for i in range(n):
        if a[i] % 2 == 0 and a[i] != -1:
            print(a[i], end = " ")
            a[i] = -1
            break
    for i in range(n):
        if a[i] != -1:
            print(a[i], end = " ")
            a[i] = -1
            break
    for i in range(n):
        if a[i] % 3 == 0 and a[i] != -1:
            print(a[i], end = " ")
            a[i] = -1
            break
    for i in range(n):
        if a[i] != -1:
            print(a[i], end = " ")
            a[i] = -1
            break


if __name__ == "__main__":
    main()