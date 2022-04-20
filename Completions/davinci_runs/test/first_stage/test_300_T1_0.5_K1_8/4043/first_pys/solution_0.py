


def main():
    n, d, k = map(int, input().split())
    if d == 1:
        if n > 1:
            print("YES")
            for i in range(2, n+1):
                print(1, i)
        else:
            print("NO")
    else:
        if n > d * k:
            print("NO")
        else:
            print("YES")
            a = []
            for i in range(1, n+1):
                if i % k == 0:
                    a.append(i)
                else:
                    a.append(i - (i % k))
            for i in range(1, n):
                print(a[i], i+1)


if __name__ == "__main__":
    main()