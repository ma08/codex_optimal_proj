
from collections import Counter

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    counter = Counter(A)
    for _ in range(M):
        B, C = map(int, input().split())
        counter[C] += B
    ans = 0
    for k, v in sorted(counter.items(), reverse=True):
        if N == 0:
            break
        elif N - v >= 0:
            ans += k * v
            N -= v
        else:
            ans += k * N
            N -= N
    print(ans)


if __name__ == '__main__':
    main()
