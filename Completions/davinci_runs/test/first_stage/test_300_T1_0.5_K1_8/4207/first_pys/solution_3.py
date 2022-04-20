

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    for i in range(len(a)):
        a[i] *= -1

    a.sort()
    b.sort()

    ans = 0
    i = 0
    j = 0
    while i < n and j < n:
        if a[i] + b[j] == 0:
            ans += 1
            i += 1
            j += 1
        elif a[i] + b[j] < 0:
            i += 1
        else:
            j += 1
    print(ans)


if __name__ == "__main__":
    main()