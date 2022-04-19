
import sys

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    assert len(a) == n

    max_len = 0
    max_len_idx = -1
    for i in range(n):
        left = 1
        right = 1

        for j in range(i, -1, -1):
            if j > 0 and a[j] > a[j-1]:
                left += 1
            else:
                break

        for j in range(i, n):
            if j < n-1 and a[j] < a[j+1]:
                right += 1
            else:
                break

        if left + right > max_len:
            max_len = left + right
            max_len_idx = i

    print(max_len)
    seq = []
    for i in range(max_len_idx, -1, -1):
        if i > 0 and a[i] > a[i-1]:
            seq.append('L')
        else:
            break

    for i in range(max_len_idx, n):
        if i < n-1 and a[i] < a[i+1]:
            seq.append('R')
        else:
            break

    print(''.join(seq))

if __name__ == '__main__':
    main()
