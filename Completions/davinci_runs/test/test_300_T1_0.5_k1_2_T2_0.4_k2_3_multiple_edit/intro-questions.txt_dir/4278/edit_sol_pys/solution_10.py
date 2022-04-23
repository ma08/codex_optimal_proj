
# My code here
def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S_sorted = [''.join(sorted(s)) for s in S]
    from collections import Counter
    C = Counter(S_sorted)
    ans = 0
    for c in C.values():
        ans += c * (c-1) // 2
    print(ans)

if __name__ == '__main__':
    main()
