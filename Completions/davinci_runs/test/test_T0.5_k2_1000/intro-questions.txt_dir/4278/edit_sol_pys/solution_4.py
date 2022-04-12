
# My code here.
def main():
    N = int(input())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    S_sort = []
    for s in S:
        S_sort.append(''.join(sorted(s)))
    from collections import Counter
    C = Counter(S_sort)
    ans = 0
    for c in C.values():
        ans += c * (c - 1) // 2
    print(ans)


if __name__ == '__main__':
    main()
