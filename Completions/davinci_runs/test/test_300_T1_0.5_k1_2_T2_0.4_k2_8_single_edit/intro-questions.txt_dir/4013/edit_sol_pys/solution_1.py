

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = min(a[-1] - a[1], a[-2] - a[0])
    print(ans)


if __name__ == "__main__":
    main()
