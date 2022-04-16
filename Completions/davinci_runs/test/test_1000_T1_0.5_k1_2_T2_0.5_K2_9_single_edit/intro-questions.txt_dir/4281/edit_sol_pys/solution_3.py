


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans_min = 1
    ans_max = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            ans_min += 1
    if a[0] != 1:
        ans_max += 1
    if a[-1] != n:
        ans_max += 1
    print(ans_min, ans_max)


if __name__ == "__main__":
    main()
