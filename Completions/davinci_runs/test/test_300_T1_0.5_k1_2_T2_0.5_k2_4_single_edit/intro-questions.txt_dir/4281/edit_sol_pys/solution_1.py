
def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    min_ans = 1
    max_ans = 1
    for i in range(1, n):
        if x[i] != x[i - 1]:
            min_ans += 1
    if x[0] != 1:
        max_ans += 1
    if x[-1] != n:
        max_ans += 1
    print(min_ans, max_ans)


if __name__ == "__main__":
    main()
