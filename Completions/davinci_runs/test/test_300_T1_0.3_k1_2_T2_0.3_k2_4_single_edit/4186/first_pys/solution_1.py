

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    while len(a) > 1:
        diff = a[0] - a[-1]
        if diff > 0:
            ans += diff
            a[-1] += diff
        else:
            a.pop()
    print(ans)

if __name__ == "__main__":
    main()