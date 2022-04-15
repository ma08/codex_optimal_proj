


def main():
    n = int(input())
    d = list(map(int, input().split()))

    left_sum = 0
    right_sum = sum(d)
    ans = 0

    for i in range(n):
        right_sum -= d[i]
        if left_sum == right_sum:
            ans = max(ans, left_sum)
        left_sum += d[i]
    print(ans)


if __name__ == '__main__':
    main()