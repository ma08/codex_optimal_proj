

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    # print(a)
    ans = 0
    while len(a) > 1:
        diff = a[-1] - a[0]
        if diff > 0:
            ans += diff
            # print(ans)
            a[0] += diff
        else:
        # print(a)
            a.pop()
    print(ans)

if __name__ == "__main__":
    main()
