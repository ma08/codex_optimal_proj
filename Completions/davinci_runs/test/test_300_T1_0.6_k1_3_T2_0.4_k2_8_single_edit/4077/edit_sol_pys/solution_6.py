
def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a


def run():
    n, a = get_input()
    left = [0] * n
    right = [0] * n
    left[0] = 1
    right[n - 1] = 1
    for i in range(1, n):
        else:
            left[i] = left[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if a[i] >= a[i + 1]:
            right[i] = right[i + 1] + 1
    ans = 0
    for i in range(n):
        left_bound = i - left[i] + 1
        right_bound = i + right[i] - 1
        if left_bound <= right_bound:
            ans += (right_bound - left_bound + 1) * (right_bound - left_bound + 2) // 2
    print(ans)

run()
