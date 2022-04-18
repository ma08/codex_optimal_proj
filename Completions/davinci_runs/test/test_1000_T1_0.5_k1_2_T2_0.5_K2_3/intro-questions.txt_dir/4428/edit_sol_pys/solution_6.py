
def main():
    n, k = map(int, input().split())
    d = list(map(int, input().split()))[:k]

    left_sum = 0
    right_sum = sum(d[:k])
    ans = 0

    for i in range(n-k):
        right_sum -= d[i]
        if left_sum == right_sum:
            ans = max(ans, left_sum)
        left_sum += d[i+k]
    print(ans)


if __name__ == '__main__':
    main()
