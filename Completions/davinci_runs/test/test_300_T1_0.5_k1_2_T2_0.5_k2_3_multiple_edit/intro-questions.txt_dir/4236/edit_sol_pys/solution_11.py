

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    l = [0] * M
    r = [0] * M
    for i in range(N):
        l[i], r[i] = map(int, input().split())
    left = [0] * (M + 1)
    right = [0] * (M + 1)
    for i in range(N):
        left[l[i]] += 1
        right[r[i]] += 1
    counter = 0
    for i in range(1, M + 1):
        if left[i] == right[i]:
            counter += 1
        elif left[i] > right[i]:
            print('#{} {}'.format(tc, counter))
            break
    else:
        print('#{} {}'.format(tc, counter))
