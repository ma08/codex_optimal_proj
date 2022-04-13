
def main():
    n = int(input())
    d = list(map(int, input().split()))

    left_sum = 0
    right_sum = sum(d[1:])
    ans = 0

    for i in range(1, n):
        right_sum -= d[i]
        if left_sum == right_sum:
            ans = max(ans, left_sum)
        left_sum += d[i]
    print(ans)


if __name__ == '__main__':
    main()
