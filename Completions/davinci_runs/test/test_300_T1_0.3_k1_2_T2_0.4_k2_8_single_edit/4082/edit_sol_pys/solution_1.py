
def solve(n, a):
    if n == 1:
        return 1

    if n == 2:
        if a[0] == a[1]:
            return 1
        else:
            return 2

    max_len = 1
    curr_len = 1
    for i in range(1, n-1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            curr_len += 1
        else:
            max_len = max(max_len, curr_len)

    if a[n - 1] > a[n - 2]:
        curr_len += 1

    max_len = max(max_len, curr_len)

            curr_len = 1
    return max(max_len, curr_len)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
