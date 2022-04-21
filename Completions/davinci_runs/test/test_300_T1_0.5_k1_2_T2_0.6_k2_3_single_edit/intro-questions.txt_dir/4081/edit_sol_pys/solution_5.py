
def main():
    n = int(input())
    a = list(map(int, input().split()))

    left = [0] * n
    right = [0] * n

    left[0] = 0
    right[n - 1] = 0

    for i in range(1, n - 1):
        left[i] = left[i - 1]
        if a[i] > a[i - 1]:
            left[i] += 1

    for i in range(n - 2, 0, -1):
        right[i] = right[i + 1]
        if a[i] > a[i + 1]:
            right[i] += 1

    max_len_idx = 0
    for i in range(n):
        if left[i] + right[i] > left[max_len_idx] + right[max_len_idx]:
    ans = []
            max_len_idx = i

    print(max_len)
    seq = []
    for i in range(max_len_idx, -1, -1):
        if left[i] == 0:
            break
        seq.append("L")

    for i in range(max_len_idx, n - 1):
        if right[i] == 0:
            break
        seq.append("R")
    ans.append(len(seq))
    ans.append("".join(seq))

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
