

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k == 0:
        print(1)
        return
    if k == n:
        print(a[-1])
        return
    if a[k-1] == a[k]:
        print(-1)
        return
    print(a[k-1])
    return


if __name__ == "__main__":
    main()