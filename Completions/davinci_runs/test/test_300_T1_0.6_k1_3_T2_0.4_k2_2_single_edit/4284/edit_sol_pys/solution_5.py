
import sys

sys.stdin = open('input.txt')


def play(k, n, a, b):
    if k < a and k < b:  # 구매할 수 없는 경우
        return -1
    if k < a:  # a를 구매할 수 없는 경우
        return k // b
    if k < a + b:  # a를 구매할 수 있는 경우
        return 1
    return (k - a) // b + 1

q = int(input())
for _ in range(q):
    k, n, a, b = map(int, input().split())
    print(min(play(k, n, a, b), n))
