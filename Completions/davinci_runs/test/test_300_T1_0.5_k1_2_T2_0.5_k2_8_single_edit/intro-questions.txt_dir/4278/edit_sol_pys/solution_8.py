
# My code here
def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for _ in range(N):
        S[i] = ''.join(sorted(S[i]))
    S_sort = []
    from collections import Counter
    C = Counter(S)
    ans = 0
    for c in C.values():
        ans += c * (c-1) // 2
    print(ans)

if __name__ == '__main__':
    main()
