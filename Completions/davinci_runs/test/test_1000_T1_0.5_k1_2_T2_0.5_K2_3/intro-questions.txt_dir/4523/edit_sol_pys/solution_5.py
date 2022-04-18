def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = set(a)
    b = set(b)
    c = list(a.intersection(b))
    if len(c) == 0:
        print("NO")
    else:
        print("YES")
        print(1, c[0])


if __name__ == "__main__":
    main()
