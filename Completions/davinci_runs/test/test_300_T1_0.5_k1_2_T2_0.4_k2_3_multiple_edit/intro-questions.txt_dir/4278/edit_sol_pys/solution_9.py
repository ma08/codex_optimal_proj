from collections import Counter


def main():
    N = int(input())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    S_sorted = []
    for s in S:
        S_sorted.append(''.join(sorted(s)))
    C = Counter(S_sorted)
    ans = 0
    for c in C.values():
        ans += c * (c-1) // 2
    print(ans)

if __name__ == '__main__':
    main()
