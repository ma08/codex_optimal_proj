
def main():
    n = int(input())
    a = input().split()
    assert len(a) == n and all(x.isdigit() for x in a)

    left = [0] * n
    right = [0] * n

    left[0] = 1
    right[n-1] = 1

    for i in range(1, n):
        left[i] = left[i-1]
        if int(a[i]) > int(a[i-1]):
            left[i] += 1

    for i in range(n-2, -1, -1):
        right[i] = right[i+1]
        if int(a[i]) < int(a[i+1]):
            right[i] += 1

    max_len = 0
    max_len_idx = -1
    for i in range(n):
        if left[i] + right[i] > max_len:
            max_len = left[i] + right[i]

            max_len_idx = i

    print(max_len)
    seq = []
    for i in range(max_len_idx, -1, -1):
        if left[i] == 1:
            break
        seq.append('L')

    for i in range(max_len_idx, n-1):
        if right[i] == 1:
            break
        seq.append('R')

    print(' '.join(seq))

if __name__ == '__main__':
    main()
