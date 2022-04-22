
import sys

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.insert(0, 0)
    a.append(sys.maxsize)
    assert len(a) == n

    left = [1] * (n+1)
    right = [1] * (n+1)

    for i in range(1, n):
        left[i] = left[i-1]
        if a[i] > a[i-1]:
            left[i] += 1

    for i in range(n-2, -1, -1):
        right[i] = right[i+1]
        if a[i] < a[i+1]:
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

    for i in range(max_len_idx, n):
        if right[i] == 1:
            break
        seq.append('R')

    print(''.join(seq))

if __name__ == '__main__':
    main()
