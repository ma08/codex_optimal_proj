
def main():
    n = int(input())
    xs = list(map(int, input().split()))
    xs.sort()
    min_ans = 1
    max_ans = 1
    for i in range(1, n):
        if xs[i] != xs[i - 1]:
            min_ans += 1
    if xs[0] != 1:
        max_ans += 1
    if xs[-1] != n:
        max_ans += 1
    print(min_ans, max_ans)


if __name__ == "__main__":
    main()
