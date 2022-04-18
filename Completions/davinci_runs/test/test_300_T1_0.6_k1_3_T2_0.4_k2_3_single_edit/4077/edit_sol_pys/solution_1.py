
def get_input():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    return n, m, a


def run():
    n, m, a = get_input()
    left = [0] * n
    right = [0] * n
    left[0] = 1
    right[n - 1] = 1
    for i in range(1, n):
        if a[i] < a[i - 1]:
            left[i] = left[i - 1] + 1
        else:
            left[i] = 1
    for i in range(n - 2, -1, -1):
        if a[i] > a[i + 1]:
            right[i] = right[i + 1] + 1
        else:
            right[i] = 1
    ans = 0
    for i in range(n):
        l = i - left[i] + 1
        r = i + right[i] - 1
        if l <= r:
            ans += (r - l + 1) * (r - l + 2) // 2
    print(ans)

run()
