import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    assert len(a) == n, "len(a) != n"

    left_len = [0] * n
    right_len = [0] * n

    left_len[0] = 1
    right_len[n-1] = 1

    for i in range(1, n):
        left_len[i] = left_len[i-1]
        if a[i] > a[i-1]:
            left_len[i] += 1

    for i in range(n-2, -1, -1):
        right_len[i] = right_len[i+1]
        if a[i] < a[i+1]:
            right_len[i] += 1

    max_len = 0
    max_len_idx = -1
    for i in range(n):
        if left_len[i] + right_len[i] > max_len:
            max_len = left_len[i] + right_len[i]
            max_len_idx = i

    sys.stdout.write(str(max_len) + '\n')
    seq = []
    for i in range(max_len_idx, -1, -1):
        if left_len[i] == 1:
            break
        seq.append('L')

    for i in range(max_len_idx, n):
        if right_len[i] == 1:
            break
        seq.append('R')

    sys.stdout.write(''.join(seq) + '\n')

if __name__ == '__main__':
    main()
