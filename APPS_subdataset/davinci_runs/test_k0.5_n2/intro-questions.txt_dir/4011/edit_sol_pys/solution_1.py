


def main():
    n = int(input())
    a = list(input())
    f = list(map(int, input().split()))
    f_inv = {f[i - 1]: i for i in range(1, 11)}
    a = [f_inv[int(i)] for i in a]  # replace each digit with its frequency

    left = 0
    right = 0
    max_left = 0
    max_right = 0
    max_sum = 0
    curr_sum = 0
    while right < n:
        if curr_sum <= 0:
            left = right
            curr_sum = 0
        curr_sum += a[right]
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_left = left
            max_right = right
        right += 1
    a = a[:max_left] + list(reversed(a[max_left:max_right + 1])) + a[max_right + 1:]
    a = [str(i) for i in a]
    print(''.join(a))


main()
