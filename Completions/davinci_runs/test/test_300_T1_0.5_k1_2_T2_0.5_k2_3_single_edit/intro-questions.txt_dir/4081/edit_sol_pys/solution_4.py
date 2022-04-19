import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    left = [1] * n
    right = [1] * n

    for i in range(n - 1):
        if a[i] < a[i + 1]:
            left[i + 1] = left[i] + 1
    for i in range(n - 1, 0, -1):
        if a[i - 1] > a[i]:
            right[i - 1] = right[i] + 1

    max_len = 0
    idx = -1
    for i in range(n):
        if left[i] + right[i] > max_len:
            max_len = left[i] + right[i]
            max_len = left[i] + right[i]
            idx = i

    print(max_len)

    ans = []
    for i in range(idx - left[idx] + 1, idx):
        ans.append('L')
    for i in range(idx, idx + right[idx]):
        ans.append('R')

    print(''.join(ans))


if __name__ == '__main__':
    main()
