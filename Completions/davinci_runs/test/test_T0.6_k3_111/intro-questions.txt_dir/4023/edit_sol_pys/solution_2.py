
def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a_min = min(a[1:]) - 1
    c = 0
    for i in range(1, n):
        if a[i] == a[i-1]:
            c += 1
    if c > a_min and a[0] == a[n-1] and a[0] != a_min:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()
