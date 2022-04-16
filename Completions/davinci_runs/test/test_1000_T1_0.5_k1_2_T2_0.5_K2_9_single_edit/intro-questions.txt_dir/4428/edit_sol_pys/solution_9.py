

def main():
    n = int(input())
    a = list(map(int, input().split()))

    left_sum = 0
    right_sum = sum(a)
    ans = 0

    for i in range(n):
        right_sum -= a[i]
        if left_sum == right_sum:
            ans = max(ans, left_sum)
        left_sum += a[i]
    print(ans)


if __name__ == '__main__':
    main()
