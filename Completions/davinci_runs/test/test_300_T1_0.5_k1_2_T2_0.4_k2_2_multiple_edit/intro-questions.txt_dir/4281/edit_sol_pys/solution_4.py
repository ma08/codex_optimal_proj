
def main():
    n = int(input())
    y = list(map(int, input().split()))
    y.sort()
    ans_min = 1
    ans_max = 1
    for i in range(1, n):
        if y[i] != y[i - 1]:
            ans_min += 1
    if y[0] != 1:
        ans_max += 1
    if y[-1] != n:
        ans_max += 1
    print(ans_min, ans_max)


if __name__ == "__main__":
    main()
