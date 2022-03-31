


def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a_min = min(a)
    if a_min == a[0]:
        a_min = a[n-1]
    c = 0
    for i in range(1, n):
        if a[i] == a[i-1]:
            c += 1
    if c > a_min:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()