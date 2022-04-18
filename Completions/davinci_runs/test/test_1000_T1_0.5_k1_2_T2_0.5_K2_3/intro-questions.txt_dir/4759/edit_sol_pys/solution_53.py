def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True


def main():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        a[i] = (a[i], i)
    a.sort(reverse=True)

    for i in range(n):
        a[i] = a[i][1]

    ans = [0] * n
    for i in range(n):
        if is_prime(i + 1):
            ans[a[i]] = i
        else:
            ans[a[i]] = i - 1

    for i in range(n):
        print(ans[i])


if __name__ == "__main__":
    main()
