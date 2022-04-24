
def main():
    n = int(input())
    x = list(map(int, input().split(' ')))
    x.sort()
    ans_min = 1
    ans_max = 1
    for i in range(1, n):
        if x[i] != x[i - 1]:
            ans_min += 1
    if x[0] != 1:
        ans_max += 1
    if x[-1] != n:
        ans_max += 1
    print(ans_min, ans_max)


if __name__ == "__main__":
    main()
